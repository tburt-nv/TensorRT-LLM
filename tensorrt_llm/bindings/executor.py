"""CPU-only stub for tensorrt_llm.bindings.executor.

All types are auto-generated via ``_stubs.make_module_getattr`` except the
one class that is called at *import* time with specific static methods.
"""

from ._stubs import _Stub, make_module_getattr


class LookaheadDecodingConfig(_Stub):
    """Override: ``llm_args.py`` reads these defaults at class-definition time."""

    @staticmethod
    def get_default_lookahead_decoding_window():
        return 4

    @staticmethod
    def get_default_lookahead_decoding_ngram():
        return 3

    @staticmethod
    def get_default_lookahead_decoding_verification_set():
        return 4


__getattr__ = make_module_getattr(__name__)
