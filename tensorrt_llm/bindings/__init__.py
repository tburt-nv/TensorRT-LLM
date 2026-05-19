"""CPU-only stub for tensorrt_llm.bindings.

This module provides minimal stub types so that the tensorrt_llm Python package
can be imported on machines without GPU or compiled C++ bindings.  Only the
symbols that appear in the top-level import chain are defined here; runtime
code that actually needs the real bindings will still fail at call-time, which
is the expected behavior on a CPU-only machine.
"""

import enum


class DataType(enum.IntEnum):
    FLOAT = 0
    HALF = 1
    INT8 = 2
    INT32 = 3
    BOOL = 4
    UINT8 = 5
    FP8 = 6
    BF16 = 7
    INT64 = 8
    INT4 = 9
    FP4 = 10


class KVCacheType(enum.Enum):
    CONTINUOUS = "CONTINUOUS"
    PAGED = "PAGED"
    DISABLED = "DISABLED"


class GptJsonConfig:

    def __init__(self, *args, **kwargs):
        raise NotImplementedError(
            "GptJsonConfig requires compiled C++ bindings")


class WorldConfig:

    def __init__(self, *args, **kwargs):
        raise NotImplementedError("WorldConfig requires compiled C++ bindings")


class ModelConfig:

    def __init__(self, *args, **kwargs):
        raise NotImplementedError("ModelConfig requires compiled C++ bindings")


class CudaStream:

    def __init__(self, *args, **kwargs):
        raise NotImplementedError("CudaStream requires compiled C++ bindings")


class MpiComm:

    def __init__(self, *args, **kwargs):
        raise NotImplementedError("MpiComm requires compiled C++ bindings")


class LoraModule:

    def __init__(self, *args, **kwargs):
        raise NotImplementedError("LoraModule requires compiled C++ bindings")


def ipc_nvls_supported(*args, **kwargs):
    return False


def __getattr__(name):
    """Return a stub class for any attribute not explicitly defined."""

    class _Stub:

        def __init__(self, *args, **kwargs):
            raise NotImplementedError(
                f"tensorrt_llm.bindings.{name} requires compiled C++ bindings")

        def __init_subclass__(cls, **kw):
            pass

    _Stub.__name__ = _Stub.__qualname__ = name
    return _Stub
