# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from setuptools import Extension, Feature

import platform
import sys

speedups = Feature(
    "optional C speed-enhancements",
    standard = True,
    ext_modules = [
        Extension('tonnikala.runtime._buffer', ['tonnikala/runtime/_buffer.c']),
    ]
)

extra_kw = dict(features={'speedups': speedups })

requires = """
    six>=1.4.1
    markupsafe>=0.18
    slimit>=0.8.1
    ply<3.6.0
""".split()

if sys.version_info < (2, 7):
    requires.append('ordereddict')


setup(
    name='tonnikala',
    version='0.20',
    description='Python templating engine - the one ton solution',
    author='Antti Haapala',
    author_email='antti@haapala.name',
    url='https://github.com/ztane/Tonnikala',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pyramid",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Text Processing :: Markup",
        "Topic :: Text Processing :: Markup :: HTML"
    ],
    scripts=['bin/tonnikala-compile-jstemplate'],
    install_requires=requires,
    setup_requires=[],
    include_package_data=True,
    packages=find_packages(),
    test_suite = "tonnikala.tests.test_all",
    tests_require=[],
    **extra_kw
)
