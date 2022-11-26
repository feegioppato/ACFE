# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 23:07:12 2022

@author: Fernando Gioppato
"""
from setuptools import setup, find_packages

setup(
      author = 'Fernando Augusto Gioppato',
      description = 'package designed for financial analysis of companies listed on the brazilian stock market (B3)',
      name = 'acfe',
      version = '0.2.1',
      packages = find_packages(include = ['acfe', 'acfe.*'])
      )