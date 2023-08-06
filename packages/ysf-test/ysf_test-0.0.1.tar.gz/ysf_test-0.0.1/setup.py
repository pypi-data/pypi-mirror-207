#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
time: 2023/5/8 15:40
file: setup.py
author: yisifan
email: yisifan@datagrand.com
"""
import setuptools

setuptools.setup(
    name="ysf_test",
    version="0.0.1",
    author="yisifan",
    description="a small example package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)