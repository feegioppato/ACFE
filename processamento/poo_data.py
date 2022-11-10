# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:18:34 2022

@author: Fernando Gioppato
"""
import re
import os
import tika
from tika import parser
import pandas as pd


class Extractor:
    
    def __init__(self, filepath, s, e):
        self.filepath = filepath
        self.startpoint = s
        self.endpoint = e
    
    def read_file(self):
        self.parsed = parser.from_file(self.filepath)
        return self.parsed
    
    def raw_content(self):
        self.content = (self.read_file())['content']
        return self.content

    def unstructured_data(self):
        pattern = re.compile(f"(?<={self.startpoint}).*(?={self.endpoint})", re.DOTALL)
        search_object = re.search(pattern, self.raw_content())
        return search_object.group(0)
    
    def data(self):
        pattern = r'''
        (?P<numero_conta>\d(?:\.\d{1,2})*)\s
        (?P<nome_conta>(?:[a-zA-Zâãõçíó\-\)\(]+\s)+)
        (?P<primeiro_ano>-?\d{1,3},?(?:,?\.?\d{1,3})*)*\s
        (?P<segundo_ano>-?\d{1,3},?(?:,?\.?\d{1,3})*)*\s
        (?P<terceiro_ano>-?\d{1,3}(?:,?\.?\d{1,3})*)'''
        
        p = re.compile(pattern, re.X)
        
        results_dict = []
        for match in re.finditer(p, self.unstructured_data()):
            (results_dict).append(match.groupdict())
        
        self.structured_data = pd.DataFrame(results_dict)
        
        return self.structured_data
        
    def data_prep(self):
        
        
        










