# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:56:04 2022

@author: Fernando Gioppato
"""

import data_extractor

filepath = 'Demonstrativos Ambev (2017, 2018, 2019).pdf'
p1 = 'PÁGINA: 2 DE 137'
p2 = 'PÁGINA: 9 DE 137'

df = data_extractor.read_pdf(filepath, p1, p2)