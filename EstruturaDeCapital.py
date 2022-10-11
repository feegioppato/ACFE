# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 23:37:22 2021

@author: ferna
"""

import pandas as pd


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
        

def ce(anos, df):
    
    ndict = {}
    
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '2.01']['valor'])
        x2 = float(x[x['cd'] == '2.02']['valor'])
        ce = (x1/(x1+x2))*100
        ndict.update({ano: round(ce, 2)})
        
    return ndict


def ipl(anos, df):
    
    ndict = {}
    
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '1.02']['valor'])
        x2 = float(x[x['cd'] == '1.01.02']['valor'])
        x3 = float(x[x['cd'] == '2.03']['valor'])
        ipl = ((x1 - x2)/x3)*100
        ndict.update({ano: round(ipl, 2)})
    return ndict


def ccp(anos, df):
    
    ndict = {}
    
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '2.03']['valor'])
        x2 = float(x[x['cd'] == '1.02']['valor'])
        ccp = (x1 - x2)
        ndict.update({ano : round(ccp, 2)})
    return ndict

def ccl(anos, df):
    
    ndict = {}
    
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '2.02']['valor'])
        x2 = float(x[x['cd'] == '2.03']['valor'])
        x3 = float(x[x['cd'] == '1.02']['valor'])
        ccl = ((x1 + x2) - x3) * 100
        ndict.update({ano: round(ccl, 2)})   
    return ndict


def irnc(anos, df):
    
    ndict = {}
    
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '1.02']['valor'])
        x2 = float(x[x['cd'] == '1.02.01']['valor'])
        x3 = float(x[x['cd'] == '2.02']['valor'])
        x4 = float(x[x['cd'] == '2.03']['valor'])
        irnc = ((x1 - x2) / (x3 + x4)) * 100
        ndict.update({ano : round(irnc, 2)})
    return ndict
