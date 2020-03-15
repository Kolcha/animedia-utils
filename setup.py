#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="animedia-utils",
    version="0.1.1",
    author="Nick Korotysh",
    author_email="kolchaprogrammer@list.ru",
    packages=setuptools.find_packages(),
    install_requires=['lxml', 'requests'],
    python_requires='>=3',
)
