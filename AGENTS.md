# AGENTS.md

## Cursor Cloud specific instructions

### Environment overview

This is **NVIDIA TensorRT-LLM** (`tensorrt_llm`), a C++/Python library for optimized LLM inference on NVIDIA GPUs. The codebase has two major layers:

- **C++ runtime** (`cpp/`) — kernels, batch manager, executor; compiled into `libtensorrt_llm.so` and Python bindings (`tensorrt_llm/bindings/`)
- **Python package** (`tensorrt_llm/`) — model definitions, LLM API, serving layer, quantization utilities

### GPU requirement

The Cloud Agent VM has **no NVIDIA GPU**. This means:

- The C++ bindings cannot be built (`python3 scripts/build_wheel.py` requires CUDA).
- `tensorrt_llm` cannot be imported at the Python level (the `__init__.py` import chain requires `tensorrt_llm.bindings`).
- Unit tests that import `tensorrt_llm` will fail with `ModuleNotFoundError`.
- Inference, model building, and serving commands (`trtllm-serve`, `trtllm-build`, `trtllm-bench`) cannot run.

### What works without GPU

- **All linting and formatting**: `pre-commit run --all-files` runs 21 hooks (isort, yapf, ruff, ruff-format, clang-format, cmake-format, codespell, autoflake, mdformat, etc.) and passes cleanly.
- **Static analysis**: `ruff check`, `ruff format --check`, `isort --check-only`, `codespell`, `mypy` (for auto_deploy files).
- **Code formatting**: `ruff format`, `yapf`, `isort`, `black` can format code.
- **Pre-commit hooks** are installed and trigger on `git commit`.

### Lint/format commands

```bash
# Run all pre-commit hooks on all files
pre-commit run --all-files

# Individual tools
ruff check                          # Lint (auto_deploy + progressively enabled files)
ruff format --check                 # Format check
isort --check-only tensorrt_llm/    # Import sorting check
codespell                           # Spell checking
```

### Testing

Most tests require a working `tensorrt_llm` import (which requires GPU + compiled bindings). To run tests in a GPU-enabled environment:

```bash
pytest tests/unittest/ -x -v
```

See `tests/README.md` and `tests/integration/README.md` for test organization details.

### Key project conventions

- Python formatting uses **yapf** (pep8, 80 cols) for most files and **ruff** (100 cols) for `auto_deploy/` and progressively enabled files. See `pyproject.toml` for the exact include lists.
- C++ code uses **clang-format** (v16+).
- Commits must include a DCO sign-off (`git commit -s`).
- PR titles follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
- The `pre-commit` config is in `.pre-commit-config.yaml`; linting config is in `pyproject.toml`.
