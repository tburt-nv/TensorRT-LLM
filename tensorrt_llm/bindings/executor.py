"""CPU-only stub for tensorrt_llm.bindings.executor.

Provides lightweight stand-in classes so that modules which *declare*
executor types (dataclass fields, type annotations, ``dir()`` introspection)
can be imported on a CPU-only machine.  Any attempt to *instantiate* an
object that genuinely needs the C++ runtime will raise ``NotImplementedError``.
"""

import enum

# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------


class BatchingType(enum.Enum):
    STATIC = 0
    INFLIGHT = 1


class CapacitySchedulerPolicy(enum.Enum):
    MAX_UTILIZATION = 0
    GUARANTEED_NO_EVICT = 1
    STATIC_BATCH = 2


class ContextChunkingPolicy(enum.Enum):
    EQUAL_PROGRESS = 0
    FIRST_COME_FIRST_SERVED = 1


class RequestType(enum.Enum):
    REQUEST_TYPE_CONTEXT_AND_GENERATION = 0
    REQUEST_TYPE_CONTEXT_ONLY = 1
    REQUEST_TYPE_GENERATION_ONLY = 2


class CommunicationType(enum.Enum):
    MPI = 0


class CommunicationMode(enum.Enum):
    LEADER = 0
    ORCHESTRATOR = 1


# ---------------------------------------------------------------------------
# Config / param dataclass-like stubs
# ---------------------------------------------------------------------------


class SamplingConfig:
    """Stub: accepts arbitrary kwargs so ``SamplingParams._get_sampling_config`` succeeds at import."""

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class OutputConfig:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class GuidedDecodingParams:

    class GuideType(enum.Enum):
        JSON = 0
        JSON_SCHEMA = 1
        REGEX = 2
        EBNF_GRAMMAR = 3
        STRUCTURAL_TAG = 4

    def __init__(self, guide_type=None, guide=None, **kwargs):
        self.guide_type = guide_type
        self.guide = guide
        for k, v in kwargs.items():
            setattr(self, k, v)


class LookaheadDecodingConfig:

    def __init__(self,
                 max_window_size=0,
                 max_ngram_size=0,
                 max_verification_set_size=0,
                 **kwargs):
        self.max_window_size = max_window_size
        self.max_ngram_size = max_ngram_size
        self.max_verification_set_size = max_verification_set_size

    @staticmethod
    def get_default_lookahead_decoding_window():
        return 4

    @staticmethod
    def get_default_lookahead_decoding_ngram():
        return 3

    @staticmethod
    def get_default_lookahead_decoding_verification_set():
        return 4


class KvCacheConfig:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class SchedulerConfig:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class PeftCacheConfig:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class ExtendedRuntimePerfKnobConfig:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class ExecutorConfig:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class DecodingConfig:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class DecodingMode:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @staticmethod
    def Auto():
        return DecodingMode()

    @staticmethod
    def TopKTopP():
        return DecodingMode()

    @staticmethod
    def BeamSearch():
        return DecodingMode()


class DynamicBatchConfig:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class EagleConfig:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class CacheTransceiverConfig:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class ContextPhaseParams:

    def __init__(self, *args, **kwargs):
        pass


class RuntimeDefaults:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class ExternalDraftTokensConfig:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


# ---------------------------------------------------------------------------
# Catch-all for any attribute not explicitly defined above
# ---------------------------------------------------------------------------


def __getattr__(name):

    class _Stub:

        def __init__(self, *args, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    _Stub.__name__ = _Stub.__qualname__ = name
    return _Stub
