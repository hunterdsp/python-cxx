def main() -> str:
    from pathlib import Path

    import subprocess
    import os

    def install_wheel(wheel_path):
        """Installs a .whl file from a specific file path using pip."""
        # Ensure the path is absolute for reliability
        abs_wheel_path = os.path.abspath(wheel_path)

        print(f"Attempting to install: {abs_wheel_path}")
        try:
            # Run pip install command
            subprocess.check_call(["uv", "pip", "install", abs_wheel_path])
            print(f"Successfully installed: {abs_wheel_path}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install the wheel file: {e}")
            # Handle installation error if necessary

    version = subprocess.check_output(
        ['uv', 'version', '--short'],text=True).strip('\n')
    projectpath = Path(__file__).parent.parent
    buildpath = projectpath.joinpath("dist")
    whlpath = buildpath.joinpath(
        f"python_cxx-{version}-cp312-cp312-linux_x86_64.whl"
    )
    print(whlpath)
    install_wheel(whlpath)

    from importlib import import_module
    from nanobind.stubgen import StubGen, load_pattern_file

    python_cxx = import_module("python_cxx")
    from python_cxx import __init__
    from __init__ import __all__

    output_file = projectpath.joinpath("src/python_cxx/_core.pyi")
    sg = StubGen(
        python_cxx,
        recursive=False,
        output_file=output_file,
        patterns=load_pattern_file(
            str(projectpath.joinpath("buildscripts/patternfile"))
        ),
    )
    for modname in __all__:
        mod = getattr(python_cxx, modname)
        sg.put(mod, modname, python_cxx)
        stub = sg.get()
        print(f"generated {modname} stub")
        print("######################################")
        print(f"{stub}")
        for pattern in sg.patterns:
            found = sg.apply_pattern(modname, mod)
            if found:
                print(f"{str(pattern)} stub matched!")
    sg.output_file.write_text(stub)


if __name__ == "__main__":
    main()
