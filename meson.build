# The first function called in each project, to initialize Meson
project(
  # Arguments
  # ---------
  'python-cxx',      # The name of the project
  'c', 'cpp',     # The languages that Meson should initialize

  # Keyword arguments:
  # ------------------
  # Strings in the form `key=value`
  default_options : ['cpp_std=c++17', 'buildtype=debugoptimized'],
  # String or array of strings describing the license(s) the code is under
  license         : 'MIT',                                
  # Takes a string or array of strings with the paths to the license file(s)
  license_files   : 'LICENSE',                                
  # Takes a string describing which Meson version the project requires
  meson_version   : '>=1.3.2',
  # Specifies the top level directory name that holds Meson subprojects
  subproject_dir  : 'subprojects',                                       
  # A free form string describing the version of this project
  version         : '0.1.0b2',
)

# Build Python extension module
python = import('python').find_installation()
python.install_sources(
    meson.current_source_dir() / 'src' / 'python_cxx' / '__init__.py',
    meson.current_source_dir() / 'scripts' / 'python_cxx_example.py',
)
nanobind_dep = dependency('nanobind')
mod = python.extension_module(
  'python_cxx',
  sources: [
    'src/_core.cpp',           
    'src/array.cpp',
    'src/mod/binding.cpp',
    'src/mod/typecaster.cpp',
    'src/mod/wrapper.cpp',
  ],
  dependencies: [nanobind_dep],
  install: true,
)
