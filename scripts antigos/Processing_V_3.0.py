# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 19:52:05 2021

@author: ferna
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def bp_cia(cia, anos):
    
    
    """ 
    Retorna o Balanço Patrimonial da empresa seleciona para o(s) ano(s) selecionado(s).
    Por Balanço Patrimonial entende-se a junção do Balanço Patrimonial do Ativo,
    Balanço Patrimonial do Passivo e Demonstrativos de Resultado.
    
    Parameters
    ----------
    cia: str
        Deve estar no format: "EMPRESA S.A."
        
    anos: list, str
        Deve ser coerente com a opção de anos escolhida na função url_downloader()
                        
    Returns
            -------
    bp: pd.DataFrame()
        DataFrame contendo todas as contas do Balanço Patrimonial da empresa selecionada
        para os anos selecionados.
            
    """
    
    bpa = pd.read_csv(f'Dados/dfp_cia_aberta_BPA_con_{anos[0]}-{anos[-1]}.csv')
    bpp = pd.read_csv(f'Dados/dfp_cia_aberta_BPP_con_{anos[0]}-{anos[-1]}.csv')
    dre = pd.read_csv(f'Dados/dfp_cia_aberta_DRE_con_{anos[0]}-{anos[-1]}.csv')

    
    frames = (bpa, bpp, dre)
    
    df = pd.concat(frames)   
    df = df[df['ORDEM_EXERC'] == 'ÚLTIMO']   
    df['DT_REFER'] = df['DT_REFER'].str[:4].astype(int)
    df = df[['DENOM_CIA', 'CD_CVM', 'GRUPO_DFP', 'DS_CONTA', 'CD_CONTA', 'VL_CONTA', 'DT_REFER']]
    df = df.rename(columns = {'DT_REFER' : 'data', 'CD_CONTA' : 'cd', 'VL_CONTA' : 'valor'})
    df = df[df['DENOM_CIA'] == cia]

    
    return df


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



