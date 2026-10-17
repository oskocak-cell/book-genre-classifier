Note that the general sytnax for `pytest` test *have* to include `test` in
the name. Our GitHub CI job (`.github/workflows/ci.yml`) also includes:

```yml
- run: pytest -q
```

When you invoke pytest with no arguments, it:

- Starts in the current working directory (the repo root in a GitHub Actions 
  runner).
- Recursively scans for any file that matches `test_*.py` or `*_test.py`.
- Collects and runs every test function/class it finds.

Note that **all** files that follow those naming patterns are discovered 
automatically; i.e., also files that do not live in `tests/` but do include
`test` in the name.