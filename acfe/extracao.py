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
    
    def __init__(self, filepath, s, e, anos):
        self.filepath = filepath
        self.startpoint = s
        self.endpoint = e
        self.listofyears = anos
        
    
    def _read_file(self):
        self.parsed = parser.from_file(self.filepath)
        return self.parsed
    
    
    def _raw_content(self):
        self.content = (self._read_file())['content']
        return self.content
    

    def _unstructured_data(self):
        trim_pattern = re.compile(f"(?<={self.startpoint}).*(?={self.endpoint})", re.DOTALL|re.IGNORECASE)
        search_object = (trim_pattern).search(self._raw_content())
        return search_object.group(0)
    
    
    
    def _string_data(self): # regex não captura linhas com (), /, -, etc.
        pattern = r'''
        (?P<cd>\d(?:\.\d{1,2})*)\s
        (?P<nc>(?:[a-zA-Z\u00C0-\u00ff]+\s)+)
        (?P<terceiro_ano>-?\d{1,3},?(?:,?\.?\d{1,3})*)*\s
        (?P<segundo_ano>-?\d{1,3},?(?:,?\.?\d{1,3})*)*\s
        (?P<primeiro_ano>-?\d{1,3}(?:,?\.?\d{1,3})*)'''
        
        p = re.compile(pattern, re.X)
        
        results_dict = []
        for match in re.finditer(p, self._unstructured_data()):
            (results_dict).append(match.groupdict())
            
        return results_dict
      
        
    def _data(self):
        self.structured_data = pd.DataFrame(self._string_data())
        self.structured_data.iloc[:, -3:] = self._data_convertion(self.structured_data.iloc[:, -3:])
        self.structured_data = self._column_names(self.structured_data)
        self.structured_data = self.structured_data.set_index('cd')
        
        return self.structured_data
        
    
    def _column_names(self, x):
        
       return x.rename({'terceiro_ano' : self.listofyears[0],
                        'segundo_ano' : self.listofyears[1],
                        'primeiro_ano' : self.listofyears[2]},
                        axis = 1)    
            
        
    def _data_convertion(self, x):
        
        return x.replace(['\.', ','], ['', '.'], regex = True).astype(float)










