# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='load_db',
    version='0.1.0',
    description='Downloads and prepares formula one data',
    long_description=readme,
    author='Kai Schlauersbach',
    author_email='kai.schlauersbach@stud.h-da.de',
    url='https://github.com/KaiSchl99/formulaone',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
