# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:23:20 2022

@author: Fernando Gioppato
"""
import re
import os
import tika
from tika import parser
import pandas as pd

# NÃO ESTÁ FUNCIONANDO

def read_pdf(filepath, page_1, page_2):
    
    parsed = parser.from_file(filepath)
    print('parser ok')
    
    raw_text = parsed['content']
    print('raw text ok')  
    
    interest_pages = re.search(f'(?<={page_1}).*(?={page_2})', raw_text, re.DOTALL) 
    # erro provavelmente nesta linha
    print('interest pages ok')
    
    raw_data = interest_pages.group(0)
    print('raw data ok')
    
    pattern = r'''
    (?P<numero_conta>\d(?:\.\d{1,2})*)\s
    (?P<nome_conta>(?:[a-zA-Zâãõçíó\-\)\(]+\s)+)
    (?P<primeiro_ano>-?\d{1,3},?(?:,?\.?\d{1,3})*)*\s
    (?P<segundo_ano>-?\d{1,3},?(?:,?\.?\d{1,3})*)*\s
    (?P<terceiro_ano>-?\d{1,3}(?:,?\.?\d{1,3})*)'''
    
    p = re.compile(pattern, re.X)
    
    resultados = []
    for linha in re.finditer(p, raw_data):
        resultados.append(linha.groupdict())

    # Transformando saída em um dataframe
    df = pd.DataFrame(resultados)

    return interest_pages


