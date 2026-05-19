"""Python bindings for TensorRT-LLM's C++ runtime.

When the compiled pybind11 extension (``_C``) is available and loadable, every
symbol is re-exported from it and this package behaves identically to the
monolithic ``bindings.cpython-*.so`` that older builds produced.

When the extension cannot be loaded (no GPU driver, no compiled build, etc.)
a lightweight set of Python-only stubs is activated instead so that the rest
of the ``tensorrt_llm`` package can still be imported for linting, testing
pure-Python logic, and similar CPU-only workflows.
"""

try:
    from ._C import *  # noqa: F401, F403

    _USING_STUBS = False
except ImportError:
    from ._stubs import make_module_getattr as _make_module_getattr

    __getattr__ = _make_module_getattr(__name__)
    _USING_STUBS = True
