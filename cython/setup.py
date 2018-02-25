from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

sourcefiles  = ['cython_class.pyx', 'cpp_solver.cpp']
compile_opts = ['-std=c++14']
ext=[Extension('*',
            sourcefiles,
            extra_compile_args=compile_opts,
            language='c++')]

setup(
  ext_modules=cythonize(ext)
)
