# tox-in-gh-actions

## tox in GitHub Actions


### Usage

`.github/workflows/pythontox.yml`

```yaml
name: Python tox

on:
  - push
  - pull_request

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9, "3.10"]

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: set PY
      run: echo "PY=$(python -VV | sha256sum | cut -d' ' -f1)" >> $GITHUB_ENV
    - uses: actions/cache@v2
      with:
        path: ~/.cache/pre-commit
        key: pre-commit|${{ env.PY }}|${{ hashFiles('.pre-commit-config.yaml') }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -rrequirements-gh.txt
    - name: Test with tox
      run: tox
```

`tox.ini`

```ini
[tox]
envlist = py37,py38,py39,py310,pre-commit
skipsdist = true

[gh-actions]
python =
    3.7: py37, pre-commit
    3.8: py38, pre-commit
    3.9: py39, pre-commit
    3.10: py310, pre-commit

[testenv]
deps =
    pytest
commands =
    pytest

[testenv:pre-commit]
skip_install = true
deps = pre-commit
commands = pre-commit run --all-files --show-diff-on-failure --color=always
```

`pytest.ini`

```ini
[pytest]
addopts = -v --color=yes
```


### Local test

```shell
pip install -Ur requirements-dev.txt
tox
```


### Development

```shell
pip install -Ur requirements-dev.txt
pre-commit install
```
