#! /usr/bin/env python

from setuptools import setup, find_packages

projname = "terminut"

setup(name=f"{projname}",
      version="0.0.0.1",
      description="package sniper // vast#1337",
      packages=find_packages(exclude=['tests']),
      author="vast#1337",
      url=f"http://pypi.python.org/pypi/({projname})",
      author_email="vastcord@proton.me",
      license="MIT",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Topic :: Scientific/Engineering",
          "Topic :: Scientific/Engineering :: Information Analysis",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Topic :: Scientific/Engineering :: Visualization",
          "Topic :: Software Development :: Libraries",
          "Topic :: Utilities",
      ],

      python_requires="~=3.7",

      install_requires=[
          "config4py>=0.1.0"
      ]
)
