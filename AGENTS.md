# AGENTS.md

## Cursor Cloud specific instructions

### Environment overview

This is **NVIDIA TensorRT-LLM** (`tensorrt_llm`), a C++/Python library for optimized LLM inference on NVIDIA GPUs. The codebase has two major layers:

- **C++ runtime** (`cpp/`) — kernels, batch manager, executor; compiled into `libtensorrt_llm.so` and Python bindings (`tensorrt_llm/bindings/`)
- **Python package** (`tensorrt_llm/`) — model definitions, LLM API, serving layer, quantization utilities

### GPU constraint

The Cloud Agent VM has **no NVIDIA GPU**. Inference, model building, and serving commands (`trtllm-serve`, `trtllm-build`, `trtllm-bench`) cannot run.

A Python-only stub for `tensorrt_llm/bindings/` is provided so that `import tensorrt_llm` works on CPU. Set `TRT_LLM_NO_LIB_INIT=1` to skip loading the compiled plugin `.so` files (which don't exist without a C++ build).

### Running unit tests without GPU

```bash
TRT_LLM_NO_LIB_INIT=1 python3 -m pytest \
  tests/unittest/llmapi/test_reasoning_parser.py \
  tests/unittest/llmapi/test_build_cache.py \
  tests/unittest/others/test_mapping.py \
  tests/unittest/trt/quantization/test_mode.py \
  tests/unittest/others/test_kv_cache_manager.py \
  tests/unittest/others/test_module.py \
  -v
```

Tests that import `tests/unittest/utils/util.py` call `cuda.cuInit()` at import time and cannot run without GPU.

### Lint/format commands

```bash
pre-commit run --all-files           # All 21 hooks
ruff check                           # Lint (auto_deploy + progressively enabled files)
ruff format --check                  # Format check
isort --check-only tensorrt_llm/     # Import sorting check
```

### Key project conventions

- Python formatting: **yapf** (pep8, 80 cols) for most files; **ruff** (100 cols) for `auto_deploy/` and progressively enabled files. See `pyproject.toml`.
- C++ code: **clang-format** (v16+).
- Commits must include DCO sign-off (`git commit -s`).
- PR titles follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
- Config: `.pre-commit-config.yaml` (hooks), `pyproject.toml` (linting).
