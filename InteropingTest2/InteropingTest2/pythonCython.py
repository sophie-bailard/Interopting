from distutils.core import setup
from Cython.Build import cythonize


setup(name='Hello World', ext_modules=cythonize("hello.pyx"))