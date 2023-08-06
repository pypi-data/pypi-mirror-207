#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='calcutils',
      version='0.1.2',
      description='a calcu moduel',
      author='Lahani_Allen',
      author_email='lahani_Allen@utc.com',
      url='https://github.com/calcu_utils/calcu_utils',
      include_package_data=True,
      package_data={
          # If any package contains *.txt files, include them:
          '': ['*.p'],
          'calcutils': ['calcutils/*.p'], }
      )
