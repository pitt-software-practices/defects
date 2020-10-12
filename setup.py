#!/usr/bin/env python

<<<<<<< HEAD
from distutils.core import setup
setup(name='defect',
=======
from setuptools import setup, find_packages

setup(name='defects',
>>>>>>> caa9251... remove random in requirments.txt
      version='0.1.0',
      description='Introducing Missing-linker Defects in Metal-Organic Frameworks',
      author='Meiirbek Islamov',
      author_email='mei12@pitt.edu',
      url='https://github.com/meiirbek-islamov/defects',
<<<<<<< HEAD
      packages=['defect'],
=======
      packages=find_packages(include=['defects']),
>>>>>>> caa9251... remove random in requirments.txt
      install_requires=[
          'numpy',
          'matplotlib'
      ],
)
