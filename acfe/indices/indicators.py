# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:30:04 2022

@author: Fernando Gioppato
"""
import pandas as pd
import numpy as np
from indices.data_extractor import Extractor

def pct(anos, df):
    
    ndict = {}
    
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '2.01']['valor'])
        x2 = float(x[x['cd'] == '2.02']['valor'])
        x3 = float(x[x['cd'] == '2.03']['valor'])
        pct = ((x1+x2)/x3)*100                                                                  
        ndict.update({ano : round(pct, 2)})  
    return ndict

