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
        
        self._pct_ = ( (x1+x2) / x3 ) * 100                                                                  
        
        return self._pct_
    
    def _ce(self):
        
        x1 = self.data.loc['2.01', self.listofyears]
        x2 = self.data.loc['2.02', self.listofyears]
        
        self._ce_ = ( x1 / (x1+x2) ) * 100
        
        return self._ce_
    
    def _ipl(self):
    
        x1 = self.data.loc['1.02', self.listofyears]
        x2 = self.data.loc['1.01.02', self.listofyears]
        x3 = self.data.loc['2.03', self.listofyears]
        
        self._ipl_ = ( (x1 - x2) / x3 ) * 100
        
        return self._ipl_

    def _ccp(self):
    
        x1 = self.data.loc['2.03', self.listofyears]
        x2 = self.data.loc['1.02', self.listofyears]
        
        self._ccp_ = ( x1 - x2 )
    
        return self._ccp_

    def _ccl(self):
    
        x1 = self.data.loc['2.02', self.listofyears]
        x2 = self.data.loc['2.03', self.listofyears]
        x3 = self.data.loc['1.02', self.listofyears]
        
        self._ccl_ = ( (x1 + x2) - x3 ) * 100
        
        return self._ccl_

    def _irnc(self):    
    
        x1 = self.data.loc['1.02', self.listofyears]
        x2 = self.data.loc['1.02.01', self.listofyears]
        x3 = self.data.loc['2.02', self.listofyears]
        x4 = self.data.loc['2.03', self.listofyears]
        
        self._irnc_ = ( (x1 - x2) / (x3 + x4) ) * 100
        
        return self._irnc_
    

    # Liquidez        
    def _lg(self):
    
        x1 = self.data.loc['1.01', self.listofyears]
        x2 = self.data.loc['1.02.01', self.listofyears]
        x3 = self.data.loc['2.01', self.listofyears]
        x4 = self.data.loc['2.02', self.listofyears]
        
        self._lg_ = ( (x1 + x2) / (x3 + x4) ) * 100
        
        return self._lg_

    def _lc(self):

        x1 = self.data.loc['1.01', self.listofyears]
        x2 = self.data.loc['2.01', self.listofyears]
        
        self._lc_ = ( x1 / x2 ) * 100
        
        return self._lc_

    def _ls(self):

        x1 = self.data.loc['1.01', self.listofyears]
        x2 = self.data.loc['1.01.04', self.listofyears]
        x3 = self.data.loc['2.01', self.listofyears]
        
        self._ls_ = ( (x1-x2) / x3) * 100
        
        return self._ls_
    
    
    # Prazos Médios
    
    def _pmrv(self):
    
        x1 = self.data.loc['1.01.03.01', self.listofyears]
        x2 = self.data.loc['3.01', self.listofyears] / 360
        
        self._pmrv_ = x1 / x2

        return self._pmrv_
    
    def _pmpc(self):
    
        x1 = self.data.loc['2.01.02', self.listofyears]
        x2 = self.data.loc['3.02', self.listofyears] * -1
        x3 = self.data.loc['1.01.04', self.listofyears]
        c1 = self.data.loc['1.01.04', self.listofyears].shift(-1)
        
        self._pmpc_ = x1 / ( (x2-c1+x3)  / 360 )
        
        return self._pmpc_

    def _pmre(self):
    
        x1 = self.data.loc['1.01.04', self.listofyears]
        x2 = self.data.loc['3.02', self.listofyears] * -1
        
        self._pmre_ = x1 / (x2 / 360)
        
        return self._pmre_

    def _ge(self):

        self._ge_ = 360 / self._pmre()

        return self._ge_
    
    
    # Rentabilidade
    
    def _ga(self):
    
        x1 = self.data.loc['3.01', self.listofyears]
        x2 = self.data.loc['1', self.listofyears]
        
        self._ga_ = ( x1 / x2 ) * 100
        
        return self._ga_

    def _ml(self):
    
        x1 = self.data.loc['3.11', self.listofyears]
        x2 = self.data.loc['3.01', self.listofyears]
        self._ml_ = ( x1 / x2 ) * 100
                
        return self._ml_

    def _roa(self):
    
        x1 = self.data.loc['3.11', self.listofyears]
        x2 = self.data.loc['1', self.listofyears]
        self._roa_ = ( x1 / x2 ) * 100

        
        return self._roa_

    def _roe(self):
    
        x1 = self.data.loc['3.11', self.listofyears]
        x2 = self.data.loc['2.03', self.listofyears]
        c1 = self.data.loc['2.03', self.listofyears].shift(-1)
        
        self._roe_ = ( x1 / ( (x2 + c1) / 2 ) ) * 100
       
        return self._roe_

      
    
     
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

    

    def todos(self):
        
        est = self.estrutura_de_capital()
        liq = self.liquidez()
        prm = self.prazos_medios()
        rent = self.rentabilidade()
        
        data = pd.concat([est, liq, prm, rent], axis = 0)
        
        return data