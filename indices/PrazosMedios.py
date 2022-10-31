# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 00:37:51 2021

@author: ferna
"""

# Bug para obter valores df[df['cd'] == '1.01.04]['valor']

import pandas as pd

def pmrv(anos, df):
    
    ndict = {}
    
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '1.01.03.01']['valor'])
        x2 = float(x[x['cd'] == '3.01']['valor'] / 360)
        pmrv = x1/x2
        ndict.update({ano: round(pmrv, 2)})
    return ndict

def pmpc(anos, df):
    
    ndict = {}
    
    for ano in anos[1:4]:
        x = df[df['data'] == ano]
        c = df[df['data'] == (ano+1)]
        x1 = float(x[x['cd'] == '2.01.02']['valor'])
        x2 = float(x[x['cd'] == '3.02']['valor'] * -1)
        x3 = float(x[x['cd'] == '1.01.04']['valor'])
        c1 = float(c[c['cd'] == '1.01.04']['valor'])
        pmpc = x1/((x2-c1+x3)/360)
        ndict.update({ano: round(pmpc, 2)})
    return ndict

def pmre(anos, df):
    
    ndict = {}
    
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(df[df['cd'] == '1.01.04']['valor'])
        x2 = float(df[df['cd'] == '3.02']['valor']*-1)
        pmre = x1/(x2/360)
        ndict.update({ano: round(pmre, 2)})
    return ndict

def ge(anos, df):

    ndict = {}

    for ano in anos:
        ge = 360/pmre[ano]
        ndict.update({ano: round(ge, 2)})
    return ndict



