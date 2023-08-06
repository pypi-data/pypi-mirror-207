#!/usr/bin/env python

# This is a shim to hopefully allow Github to detect the package, build is done with poetry

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="nichecompass",
        version='0.0.1',
        description="An empty package to reserve the name on PyPI",
        long_description="",
        author="Sebastian Birk",
        author_email="sebastian.birk@outlook.com",
        # url="https://github.com/sebastianbirk/nichecompass",
        packages=["nichecompass"])
