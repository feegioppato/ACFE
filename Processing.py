# -*- coding: utf-8 -*-

# Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
 


# Lendo dados

file = 'dados_klabin/klabin_bpa_2020.xlsx'
file2 = 'dados_klabin/klabin_bpp_2020.xlsx'
file3 = 'dados_klabin/klabin_dre_2020.xlsx'

'dados_klabin/klabin_bpa_2020.xlsx', 'dados_klabin/klabin_bpp_2020.xlsx', 'dados_klabin/klabin_dre_2020.xlsx'



class Demonstrativos:
    def __init__(self, file, file2, file3):
        self.file = file
        self.file2 = file2
        self.file3 = file3
    

    def read(self):
        """ Função para carregar aruivos do Balanço Patrimonial do Ativo,
            Balanço Patrimonial do Passivo e Demonstrativo de Resultados e
            organizar em um DataFrame """
            
        
        bpa = pd.read_excel(self.file, skiprows=2, skipfooter=1)
        bpp = pd.read_excel(self.file2, skiprows=2, skipfooter=1)
        dre = pd.read_excel(self.file3, skiprows=2, skipfooter=1)
        
    
        nomes = ['contas', '2020', '2019', '2018']
        drop = ['% total', '% total.1', '% total.2']
        frames = (bpa, bpp, dre)

        for frame in frames:
        
            frame.drop(drop, axis = 1, inplace = True)
            frame.columns = nomes
        
            bp = pd.concat(frames, ignore_index = True)
    
        bp = bp.set_index('contas')
        bp = bp.loc[(bp!=0).any(axis=1)]
        
        return bp


class EstruturaDeCapital(Demonstrativos):
    anos = ['2018', '2019', '2020']
        
    
    def pct(self):        
        self.ndict = {}
        for ano in self.anos:
            k = bp[ano]
            k1 = k.loc['Passivo Circulante']
            k2 = k.loc['Passivo Não Circulante']
            k3 = k.loc['Patrimônio Líquido Consolidado']
            pct = ((k1+k2)/k3)*100
            self.ndict.update({ano: round(pct, 2)})
    
        return self.ndict

    def ce(self):
        self.ndict = {}
        for ano in self.anos:
            k = bp[ano]
            k1 = k.loc['Passivo Circulante']
            k2 = k.loc['Passivo Não Circulante']
            ce = (k1/(k1+k2))*100
            self.ndict.update({ano: round(ce, 2)})
        return self.ndict

    def ipl(self):
        self.ndict = {}
        for ano in self.anos:
            k = bp[ano]
            k1 = k.loc['Ativo Não Circulante']
            k2 = k.loc['Ativo Realizável a Longo Prazo']
            k3 = k.loc['Patrimônio Líquido Consolidado']
            ipl = ((k1 - k2)/k3)*100
            self.ndict.update({ano: round(ipl, 2)})
        return self.ndict

    def ccp(self):
        self.ndict = {}
        for ano in self.anos:
            k = bp[ano]
            k1 = k.loc['Patrimônio Líquido Consolidado']
            k2 = k.loc['Ativo Não Circulante']
            ccp = k1-k2
            self.ndict.update({ano: round(ccp, 2)})
        return self.ndict

    def ccl(self):
        self.ndict = {}
        for ano in self.anos:
            k = bp[ano]
            k1 = k.loc['Patrimônio Líquido Consolidado']
            k2 = k.loc['Passivo Não Circulante']
            k3 = k.loc['Ativo Não Circulante']
            ccl = (k1+k2)-k3
            self.ndict.update({ano: round(ccl, 2)})
        return self.ndict

    def irnc(self):
        self.ndict = {}
        for ano in self.anos:
            k = bp[ano]
            k1 = k.loc['Ativo Não Circulante']
            k2 = k.loc['Ativo Realizável a Longo Prazo']
            k3 = k.loc['Patrimônio Líquido Consolidado']
            k4 = k.loc['Passivo Não Circulante']
            irnc = ((k1-k2)/(k3+k4))*100
            self.ndict.update({ano: round(irnc, 2)})
        return self.ndict













