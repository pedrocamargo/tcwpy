"""
 -----------------------------------------------------------------------------------------------------------
 Package:    TCWPy

 Name:       Auxiliary code
 Purpose:    Compiles TCWPy's Cython code

 Original Author:  Pedro Camargo (c@margo.co)
 Contributors:
 Last edited by: Pedro Camrgo

 Website:    https://github.com/pedrocamargo/tcwpy
 Repository:  https://github.com/pedrocamargo/tcwpy

 Created:    30/11/2017
 Updated:    
 Copyright:   (c) Authors
 Licence:     See LICENSE.TXT
 -----------------------------------------------------------------------------------------------------------
 """

from __future__ import division, print_function, absolute_import
import sys
sys.dont_write_bytecode = True

import numpy as np
try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

from Cython.Distutils import build_ext

import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True


ext_module = Extension(
    'mtx',
    ["mtx.pyx"],
    #extra_compile_args=['/fopenmp'],
    #extra_link_args=['/fopenmp'],
    extra_objects=['C:/Program Files/TransCAD 7.0/CaliperMTX.dll'],
    include_dirs=[np.get_include()])


setup(
      cmdclass={'build_ext': build_ext},
      ext_modules=[ext_module],
      language="c++",)
