from setuptools import setup, Extension

setup(
    #...
    ext_modules=[Extension('keyboard', ['keyboard.c'],),],
)