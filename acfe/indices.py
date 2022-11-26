# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:14:41 2022

@author: Fernando Gioppato
"""
from extracao import Extractor


class Indicadores(Extractor):
        
    def __init__(self, filepath, s, e, years):
        
        Extractor.__init__(self, filepath, s, e, years)
        self.data = self._data()


    # Estrutura de Capital
        
    def pct(self):
        
        x1 = self.data.loc['2.01', self.listofyears]
        x2 = self.data.loc['2.02', self.listofyears]
        x3 = self.data.loc['2.03', self.listofyears]
        
        self._pct = ( (x1+x2) / x3 ) * 100                                                                  
        
        return self._pct

    
    def ce(self):
        
        x1 = self.data.loc['2.01', self.listofyears]
        x2 = self.data.loc['2.02', self.listofyears]
        
        self._ce = ( x1 / (x1+x2) ) * 100
        
        return self._ce
    
    
    def ipl(self):
    
        x1 = self.data.loc['1.02', self.listofyears]
        x2 = self.data.loc['1.01.02', self.listofyears]
        x3 = self.data.loc['2.03', self.listofyears]
        
        self._ipl = ( (x1 - x2) / x3 ) * 100
        
        return self._ipl


    def ccp(self):
    
        x1 = self.data.loc['2.03', self.listofyears]
        x2 = self.data.loc['1.02', self.listofyears]
        
        self._ccp = ( x1 - x2 )
    
        return self._ccp


    def ccl(self):
    
        x1 = self.data.loc['2.02', self.listofyears]
        x2 = self.data.loc['2.03', self.listofyears]
        x3 = self.data.loc['1.02', self.listofyears]
        
        self._ccl = ( (x1 + x2) - x3 ) * 100
        
        return self._ccl


    def irnc(self):    
    
        x1 = self.data.loc['1.02', self.listofyears]
        x2 = self.data.loc['1.02.01', self.listofyears]
        x3 = self.data.loc['2.02', self.listofyears]
        x4 = self.data.loc['2.03', self.listofyears]
        
        self._irnc = ( (x1 - x2) / (x3 + x4) ) * 100
        
        return self._irnc
    

    # Liquidez    
    
    def lg(self):
    
        x1 = self.data.loc['1.01', self.listofyears]
        x2 = self.data.loc['1.02.01', self.listofyears]
        x3 = self.data.loc['2.01', self.listofyears]
        x4 = self.data.loc['2.02', self.listofyears]
        
        self._lg = ( (x1 + x2) / (x3 + x4) ) * 100
        
        return self._lg


    def lc(self):

        x1 = self.data.loc['1.01', self.listofyears]
        x2 = self.data.loc['2.01', self.listofyears]
        
        self._lc = ( x1 / x2 ) * 100
        
        return self._lc


    def ls(self):

        x1 = self.data.loc['1.01', self.listofyears]
        x2 = self.data.loc['1.01.04', self.listofyears]
        x3 = self.data.loc['2.01', self.listofyears]
        
        self._ls = ( (x1-x2) / x3) * 100
        
        return self._ls
    
    
    # Prazos Médios
    
    def _pmrv(self):
    
        x1 = self.data.loc['1.01.03.01', self.listofyears]
        x2 = self.data.loc['3.01', self.listofyears] / 360
        
        self._pmrv = x1 / x2

        return self._pmrv
    

    def _pmpc(self): # errado: variável c deve ser defasada em um ano
    
        x1 = self.data.loc['2.01.02', self.listofyears]
        x2 = self.data.loc['3.02', self.listofyears] * -1
        x3 = self.data.loc['1.01.04', self.listofyears]
        c1 = self.data.loc['1.01.04', self.listofyears]
        
        self._pmpc = x1 / ( (x2-c1+x3) / 360 )
        
        return self._pmpc


    def _pmre(self): # erro regex não capturou linha (3.02)
    
        x1 = self.data.loc['1.01.04', self.listofyears]
        x2 = self.data.loc['3.02', self.listofyears] * -1
        
        self._pmre = x1 / (x2 / 360)
        
        return self._pmre


    def _ge(self): # erro regex não capturou linha (3.02)

        self._ge = 360 / self.pmre()

        return self._ge
    
    
    # Rentabilidade
    
    def _ga(self): # erro: regex ão capturou linha (3.01)
    
        x1 = self.data.loc['3.01', self.listofyears]
        x2 = self.data.loc['1', self.listofyears]
        
        self._ga = ( x1 / x2 ) * 100
        
        return self._ga

    def _ml(self): # erro: regex não capturou linha (3.01)
    
        x1 = self.data.loc['3.11', self.listofyears]
        x2 = self.data.loc['3.01', self.listofyears]
        self._ml = ( x1 / x2 ) * 100
                
        return self._ml


    def _roa(self):
    
        x1 = self.data.loc['3.11', self.listofyears]
        x2 = self.data.loc['1', self.lisfotyears]
        self._roa = ( x1 / x2 ) * 100

        
        return self._roa



    def _roe(self): # errado: variável 'c' deve ser defasada em 01 ano
    
        x1 = self.data.loc['3.11', self.listofyears]
        x2 = self.data.loc['2.03', self.listofyears]
        c1 = self.data.lloc['2.03', self.listofyears]
        
        self._roe = ( x1 / ( (x2 + c1) / 2 ) ) * 100
       
        return self._roe

      
        
    
    
        