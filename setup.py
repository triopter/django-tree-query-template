#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='django-tree-query-template',
    version='0.1',
    description='Django template tags for django-tree-queries, borrowed from django-mptt',
    long_description="Adapted from https://github.com/django-mptt/django-mptt/blob/main/mptt/templatetags/mptt_tags.py via https://github.com/feincms/django-tree-queries/issues/29#issuecomment-1458253290",
    author='Noemi Millman',
    author_email='noemi@triopter.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=["django", "django-tree-queries"],
    license="MIT",
    zip_safe=False,
)
