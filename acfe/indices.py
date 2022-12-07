# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:14:41 2022

@author: Fernando Gioppato
"""
from extracao import Extractor
import pandas as pd


class _Indicadores(Extractor):
        
    def __init__(self, filepath, s, e, anos):
        
        Extractor.__init__(self, filepath, s, e, anos)
        self.data = self._data()

    # Estrutura de Capital
    def _pct(self):
        
        x1 = self.data.loc['2.01', self.listofyears]
        x2 = self.data.loc['2.02', self.listofyears]
        x3 = self.data.loc['2.03', self.listofyears]
        
        self._pct = ( (x1+x2) / x3 ) * 100                                                                  
        
        return self._pct
    
    def _ce(self):
        
        x1 = self.data.loc['2.01', self.listofyears]
        x2 = self.data.loc['2.02', self.listofyears]
        
        self._ce = ( x1 / (x1+x2) ) * 100
        
        return self._ce
    
    def _ipl(self):
    
        x1 = self.data.loc['1.02', self.listofyears]
        x2 = self.data.loc['1.01.02', self.listofyears]
        x3 = self.data.loc['2.03', self.listofyears]
        
        self._ipl = ( (x1 - x2) / x3 ) * 100
        
        return self._ipl

    def _ccp(self):
    
        x1 = self.data.loc['2.03', self.listofyears]
        x2 = self.data.loc['1.02', self.listofyears]
        
        self._ccp = ( x1 - x2 )
    
        return self._ccp

    def _ccl(self):
    
        x1 = self.data.loc['2.02', self.listofyears]
        x2 = self.data.loc['2.03', self.listofyears]
        x3 = self.data.loc['1.02', self.listofyears]
        
        self._ccl = ( (x1 + x2) - x3 ) * 100
        
        return self._ccl

    def _irnc(self):    
    
        x1 = self.data.loc['1.02', self.listofyears]
        x2 = self.data.loc['1.02.01', self.listofyears]
        x3 = self.data.loc['2.02', self.listofyears]
        x4 = self.data.loc['2.03', self.listofyears]
        
        self._irnc = ( (x1 - x2) / (x3 + x4) ) * 100
        
        return self._irnc
    

    # Liquidez        
    def _lg(self):
    
        x1 = self.data.loc['1.01', self.listofyears]
        x2 = self.data.loc['1.02.01', self.listofyears]
        x3 = self.data.loc['2.01', self.listofyears]
        x4 = self.data.loc['2.02', self.listofyears]
        
        self._lg = ( (x1 + x2) / (x3 + x4) ) * 100
        
        return self._lg

    def _lc(self):

        x1 = self.data.loc['1.01', self.listofyears]
        x2 = self.data.loc['2.01', self.listofyears]
        
        self._lc = ( x1 / x2 ) * 100
        
        return self._lc

    def _ls(self):

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
    
    def _pmpc(self):
    
        x1 = self.data.loc['2.01.02', self.listofyears]
        x2 = self.data.loc['3.02', self.listofyears] * -1
        x3 = self.data.loc['1.01.04', self.listofyears]
        c1 = self.data.loc['1.01.04', self.listofyears].shift(-1)
        
        self._pmpc = x1 / ( (x2-c1+x3)  / 360 )
        
        return self._pmpc

    def _pmre(self):
    
        x1 = self.data.loc['1.01.04', self.listofyears]
        x2 = self.data.loc['3.02', self.listofyears] * -1
        
        self._pmre = x1 / (x2 / 360)
        
        return self._pmre

    def _ge(self):

        self._ge = 360 / self._pmre

        return self._ge
    
    
    # Rentabilidade
    
    def _ga(self):
    
        x1 = self.data.loc['3.01', self.listofyears]
        x2 = self.data.loc['1', self.listofyears]
        
        self._ga = ( x1 / x2 ) * 100
        
        return self._ga

    def _ml(self):
    
        x1 = self.data.loc['3.11', self.listofyears]
        x2 = self.data.loc['3.01', self.listofyears]
        self._ml = ( x1 / x2 ) * 100
                
        return self._ml

    def _roa(self):
    
        x1 = self.data.loc['3.11', self.listofyears]
        x2 = self.data.loc['1', self.listofyears]
        self._roa = ( x1 / x2 ) * 100

        
        return self._roa

    def _roe(self):
    
        x1 = self.data.loc['3.11', self.listofyears]
        x2 = self.data.loc['2.03', self.listofyears]
        c1 = self.data.loc['2.03', self.listofyears].shift(-1)
        
        self._roe = ( x1 / ( (x2 + c1) / 2 ) ) * 100
       
        return self._roe

      
    
     
class Indicadores(_Indicadores):
    
    
    def __init__(self, filepath, s, e, anos):
      
        super().__init__(filepath, s, e, anos)
                          
        
    

    def _to_df(self, idx, val):
         
         df = pd.DataFrame(data = val, index = idx, columns = self.listofyears)
         
         return df

        
                    
    def estrutura_de_capital(self):
        
        idx = ['Participação de Cappital de Terceiros', 
               'Composição do Endividamento',
               'Imobilização do Patrimônio Líquido',
               'Capital Circulante Próprio',
               'Capital Circulante Líquido',
               'Imobilização de Recursos Não Correntes']
    

        data = self._to_df( idx = idx, val = [self._pct(),
                                               self._ce(),
                                               self._ipl(),
                                               self._ccp(),
                                               self._ccl(),
                                               self._irnc()] )

        
        return data
        
    
    def liquidez(self):
        
        idx = ['Liquidez Geral',
               'Liquidez Corrente',
               'Liquidez Seca']
        
        data = self._to_df( idx = idx, val = [self._lg(),
                                              self._lc(),
                                              self._ls()] )
        
        return data

    def prazos_medios(self):
        
        idx = ['Prazo Médio de Recebimento de Vendas',
               'Prazo Médio de Pagamento de Contas', 
               'Prazo Médio de Renovação de Estoques',
               'Giro do Estoque']

        data = self._to_df (idx = idx, val = [self._pmrv(),
                                              self._pmpc(),
                                              self._pmre(),
                                              self._ge()])
         
        return data

        
    
    def rentabilidade(self):
        
        idx = ['Giro do Ativo', 
               'Margem Líquida',
               'Rentabilidade do Ativo (ROA)',
               'Rentabilidade do Patrimônio Líquido (ROE)']


        data = self._to_df(idx = idx, val = [self._ga(),
                                             self._ml(),
                                             self._roa(),
                                             self._roe()])
        
        return data

    