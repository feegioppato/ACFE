# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 23:38:14 2021

@author: ferna
"""

import pandas as pd


def lg(anos, df):
    
    ndict = {}
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '1.01']['valor'])
        x2 = float(x[x['cd'] == '1.02.01']['valor'])
        x3 = float(x[x['cd'] == '2.01']['valor'])
        x4 = float(x[x['cd'] == '2.02']['valor'])
        lg = ((x1 + x2) / (x3 + x4)) * 100
        ndict.update({ano : round(lg, 2)})
        
    return ndict

def lc(anos, df):

    ndict = {}
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '1.01']['valor'])
        x2 = float(x[x['cd'] == '2.01']['valor'])
        lc = (x1/x2)*100
        ndict.update({ano: round(lc, 2)})
    return ndict


def ls(anos, df):

    ndict = {}
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '1.01']['valor'])
        x2 = float(x[x['cd'] == '1.01.04']['valor'])
        x3 = float(x[x['cd'] == '2.01']['valor'])
        ls = ((x1-x2)/x3)*100
        ndict.update({ano: round(ls, 2)})
    return ndict


