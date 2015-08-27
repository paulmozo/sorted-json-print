# encoding: utf-8

from setuptools import setup
import os.path

setup(
    name="sorted_print",
    version="1.0.0",
    author="Paul Mozo",
    author_email="paul.mozo@datasift.com",
    description="Simple module for printing arbitrarily ordered JSON according to a strict config",
    url="https://github.com/paulmozo/sorted-json-print",
    packages=['sorted_print', 'sorted_print.configs']
)
