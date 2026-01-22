#!/usr/bin/env python
#
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "benchmarkme",
#     "numpy>=2.3",
#     "python-cxx",
# ]
#
# [tool.uv.sources]
# benchmarkme = { git = "https://github.com/hunterdsp/benchmarkme.git" }
# python-cxx = { path = "." }
# ///


def main() -> None:

    # Import sub-packages
    import numpy as np

    import python_cxx as m
    from benchmarkme import BenchMark

    x = [1, 2, 3]
    print()
    print("---------------------------------------------------------")
    print("Hello from python_cxx!!!")
    print("A C++ compiled extension that can operate in Python.")
    print(f"For example, given a list {x}...one can use:")
    print("---------------------------------------------------------")
    print(f"* Typecasting to e.g. square: {m.square_it(x)}")
    print(f"* Binding to e.g. double: {m.double_it(x)}")
    print(f"* Or wrap an operation like decrement: {m.decrement_it(x)}!")
    x = np.ones(5, dtype=np.complex128)
    print(f"Executing a C++ class method on {x.real} gives:")
    ema = m.ExpAverage()
    ema.step(x)
    print(f"Exponential average: {x.real}")
    samples = 102400
    x = np.ones(samples, dtype=np.complex128)
    bmk = BenchMark(
        f=ema.step,
        fargs=[
            "x",
        ],
        items_processed=samples,
        namespace={"np": np, "samples": samples, "x": x},
    )
    print()
    bmk()


if __name__ == "__main__":
    main()
