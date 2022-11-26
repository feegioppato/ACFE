# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:14:41 2022

@author: Fernando Gioppato
"""
from data_extractor import Extractor


class Indicadores(Extractor):
    
    def __init__(self):
        
        self.data = self._data()
        
        super().__init__(self)
        

