# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 00:00:04 2021

@author: ferna
"""
import pandas as pd

def ga(anos, df):
    
    ndict = {}
    
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '3.01']['valor'])
        x2 = float(x[x['cd'] == '1']['valor'])
        ga = (x1/x2)*100
        ndict.update({ano: round(ga, 2)})
        
    return ndict

def ml(anos, df):
    
    ndict = {}
    
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '3.11']['valor'])
        x2 = float(x[x['cd'] == '3.01']['valor'])
        ml = (x1/x2)*100
        ndict.update({ano: round(ml, 2)})
        
    return ndict


def roa(anos, df):
    
    ndict = {}
    
    for ano in anos:
        x = df[df['data'] == ano]
        x1 = float(x[x['cd'] == '3.11']['valor'])
        x2 = float(x[x['cd'] == '1']['valor'])
        roa = (x1/x2)*100
        ndict.update({ano: round(roa, 2)})
        
    return ndict



def roe(anos, df):
    
    ndict = {}
    
    for ano in anos[1:4]:
        x = df[df['data'] == ano]
        c = df[df['data'] == (ano+1)]
        x1 = float(x[x['cd'] == '3.11']['valor'])
        x2 = float(x[x['cd'] == '2.03']['valor'])
        c1 = float(x[x['cd'] == '2.03']['valor'])
        roe = (x1/((x2+c1)/2))*100
        ndict.update({ano : round(roe, 2)})
    return ndict