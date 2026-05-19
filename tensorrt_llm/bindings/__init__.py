"""CPU-only stub for tensorrt_llm.bindings.

Provides auto-generated stand-in types so the Python package can be imported
on machines without compiled C++ bindings.  See ``_stubs.py`` for the shared
machinery used by every submodule in this package.
"""

from ._stubs import make_module_getattr

__getattr__ = make_module_getattr(__name__)
