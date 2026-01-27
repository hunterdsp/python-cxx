# python-cxx

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fhunterdsp%2Fpython-cxx%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/python-cxx)
![Build](https://img.shields.io/github/actions/workflow/status/hunterdsp/python-cxx/build_test_upload.yml)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/python-cxx)
![GitHub License](https://img.shields.io/github/license/hunterdsp/python-cxx)

C/C++ DSP Extensions for Python.

Building the foundation for a fast, reliable, easy-to-use signal processing
toolset.

This package is about real-world utility, learning, and most of all fun!

## Installation & Usage

```{console=}
pip install python-cxx
```

Once the package has been installed you can run the example with

```{cosole=}
python-cxx-example
```

If successful, you should see something like this

```{console=}
---------------------------------------------------------
Hello from python_cxx!!!
A C++ compiled extension that can operate in Python.
For example, given a list [1, 2, 3]...one can use:
---------------------------------------------------------
* Typecasting to e.g. square: python_cxx.IntVector([1, 4, 9])
* Binding to e.g. double: python_cxx.IntVector([2, 4, 6])
* Or wrap an operation like decrement: [0, 1, 2]!
Executing a C++ class method on [1. 1. 1. 1. 1.] gives:
Exponential average: [0.9     0.99    0.999   0.9999  0.99999]

Benchmark Results
-----------------
* Ran 100 trials 5 times.
* Time of one independent trial: 2.92 msec
* Best time of subsequent trials: 2.7 msec
* Worst time of subsequent trials: 2.92 msec
* Best speed: 152 Mitems / sec
* Worst speed: 140 Mitems / sec
```

Experiment with the example script (`python-cxx/example.py`), use with the
interpreter, or get the source and add your own features!

```{python}
>>> import numpy as np
>>> from python_cxx import decrement_it
>>> x = [1, 2, 3]
>>> decrement_it(x)
[0, 1, 2]
```

## Source Installation & Development

### Install

[Get `uv`](https://docs.astral.sh/uv/getting-started/installation/)

```{console=}
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Get the code and go to the project directory

```{console=}
git clone https://github.com/hunterdsp/python-cxx.git && cd python-cxx
```

Synchronize dependencies and install

```{console=}
uv sync
```

### Develop

- Edit the code
- Add testing
- Commit!
- Synchronize: `uv sync`
- Run scripts e.g.: `uv run --no-editable python-cxx-example`
- Ensure ALL tests pass: `uvx pytest`
- Repeat until you make it here with no failures
- Submit a pull-request

... more coming soon ... **Have Fun!!!**
