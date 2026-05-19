"""CPU-only stub for tensorrt_llm.bindings.internal.userbuffers."""


def __getattr__(name):

    class _Stub:

        def __init__(self, *args, **kwargs):
            raise NotImplementedError(
                f"tensorrt_llm.bindings.internal.userbuffers.{name} requires compiled C++ bindings"
            )

    _Stub.__name__ = _Stub.__qualname__ = name
    return _Stub
