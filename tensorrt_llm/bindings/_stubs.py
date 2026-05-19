"""Generic stub machinery for CPU-only bindings.

Every stub module in this package delegates to the same small set of
primitives defined here, so there is exactly one place to maintain.

*  ``_StubMeta``  – metaclass whose ``__getattr__`` auto-vivifies new
   stub classes for any attribute access (``SomeStub.Foo`` → new class).
*  ``_Stub``      – base class that accepts arbitrary ``*args / **kwargs``.
*  ``make_module_getattr`` – returns a module-level ``__getattr__`` that
   creates a fresh ``_Stub`` subclass for every unknown name.
"""


class _StubMeta(type):
    """Metaclass that auto-generates a child stub for any attribute access.

    Pybind11 enums expose ``__members__``; the stub returns an empty dict
    so that decorators like ``mirror_pybind_enum`` see zero fields to check.
    """

    def __getattr__(cls, name):
        if name == "__members__":
            return {}
        if name.startswith("_"):
            raise AttributeError(name)
        child = _StubMeta(name, (_Stub, ), {})
        setattr(cls, name, child)
        return child


class _Stub(metaclass=_StubMeta):
    """Base stub: stores constructor kwargs as instance attributes."""

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __init_subclass__(cls, **kw):
        super().__init_subclass__(**kw)


def make_module_getattr(module_path):
    """Return a ``__getattr__`` suitable for a stub module.

    Unknown names are resolved to unique ``_Stub`` subclasses that are
    cached so repeated access returns the same class object (important
    for identity checks and dict keys).
    """
    cache = {}

    def __getattr__(name):
        if name not in cache:
            cache[name] = _StubMeta(name, (_Stub, ), {})
        return cache[name]

    return __getattr__
