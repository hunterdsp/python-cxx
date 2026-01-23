# python-cxx

C/C++ DSP Extensions for Python.

## Installation

[With `uv`](https://docs.astral.sh/uv/getting-started/installation/)
(install `uv` with `curl -LsSf https://astral.sh/uv/install.sh | sh`)

```{console=}
uv install git+github.com/hunterdsp/python-cxx.git
```

or `pip`

```{console=}
python3 -m venv .venv && . .venv/bin/activate
pip install git+github.com/hunterdsp/python-cxx.git
```

## Usage

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
interpreter, or add your own features!

```{python}
>>> import numpy as np
>>> from python_cxx import decrement_it
>>> x = [1, 2, 3]
>>> decrement_it(x)
[0, 1, 2]
```

## Source Installation

Get the code and move into the project directory

```{console=}
git clone https://github.com/hunterdsp/python-cxx.git && cd python-cxx
```

Install with `uv` (recommended)

```{console=}
uv sync
```

or `pip`

```{console=}
python3 -m venv .venv && . .venv/bin/activate
pip install .
```

## For Developers

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
- Submit a pull-request!




... more coming soon ... **Have Fun!!!**
