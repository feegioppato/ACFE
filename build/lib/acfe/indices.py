# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:14:41 2022

@author: Fernando Gioppato
"""
from acfe.extracao import Extractor
from acfe import utils
import pandas as pd


class _Indicadores(Extractor):
    
    """ Helper class used to calculate each index individually. """
        
    def __init__(self, filepath, s, e, anos):
        
        """ Initializes class.
        
        Inherits attributes from Extractor parent class and sets the 'data' attribute. """
        
        Extractor.__init__(self, filepath, s, e, anos)
        self.data = self._data()
        
        try:
            if self.data.index.isin(utils.cds) == True:
                pass
            
            else:
                raise ValueError()
                
        except:
            print('Data does not contain all accounts, consider choosing another company to avoid erros')
                

    # Estrutura de Capital
    def _pct(self):
        
        """ Private method used to calculate the Participação de Capital de Terceiros index. """
        
        x1 = self.data.loc[utils.cds[7], self.listofyears]
        x2 = self.data.loc[utils.cds[9], self.listofyears]
        x3 = self.data.loc[utils.cds[10], self.listofyears]
        
        self._pct_ = ( (x1+x2) / x3 ) * 100                                                                  
        
        return self._pct_
    
    def _ce(self):
        
        """ Private method used to calculate the Composição do Endividamento index. """
        
        x1 = self.data.loc[utils.cds[7], self.listofyears]
        x2 = self.data.loc[utils.cds[9], self.listofyears]
        
        self._ce_ = ( x1 / (x1+x2) ) * 100
        
        return self._ce_
    
    def _ipl(self):
        
        """ Private method used to calculate the Imobilização do Patrimônio Líquido index. """
    
        x1 = self.data.loc[utils.cds[5], self.listofyears]
        x2 = self.data.loc[utils.cds[2], self.listofyears]
        x3 = self.data.loc[utils.cds[10], self.listofyears]
        
        self._ipl_ = ( (x1 - x2) / x3 ) * 100
        
        return self._ipl_

    def _ccp(self):
        
        """ Private method used to calculate the Capital Circulante Próprio index. """
    
        x1 = self.data.loc[utils.cds[10], self.listofyears]
        x2 = self.data.loc[utils.cds[5], self.listofyears]
        
        self._ccp_ = ( x1 - x2 )
    
        return self._ccp_

    def _ccl(self):
        
        """ Private method used to calculate the Capital Circulante Líquido index. """
    
        x1 = self.data.loc[utils.cds[9], self.listofyears]
        x2 = self.data.loc[utils.cds[10], self.listofyears]
        x3 = self.data.loc[utils.cds[5], self.listofyears]
        
        self._ccl_ = ( (x1 + x2) - x3 ) * 100
        
        return self._ccl_

    def _irnc(self):    
    
        """ Private method used to calculate the Imobilização de Recursos Não Correntes index. """    
    
        x1 = self.data.loc[utils.cds[5], self.listofyears]
        x2 = self.data.loc[utils.cds[2], self.listofyears]
        x3 = self.data.loc[utils.cds[9], self.listofyears]
        x4 = self.data.loc[utils.cds[10], self.listofyears]
        
        self._irnc_ = ( (x1 - x2) / (x3 + x4) ) * 100
        
        return self._irnc_
    

    # Liquidez        
    def _lg(self):
        
        """ Private method used to calculate the Liquidez Geral index. """
    
        x1 = self.data.loc[utils.cds[1], self.listofyears]
        x2 = self.data.loc[utils.cds[2], self.listofyears]
        x3 = self.data.loc[utils.cds[7], self.listofyears]
        x4 = self.data.loc[utils.cds[9], self.listofyears]
        
        self._lg_ = ( (x1 + x2) / (x3 + x4) ) * 100
        
        return self._lg_

    def _lc(self):

        """ Private method used to calculate the Liquidez Corrente index. """            

        x1 = self.data.loc[utils.cds[2], self.listofyears]
        x2 = self.data.loc[utils.cds[7], self.listofyears]
        
        self._lc_ = ( x1 / x2 ) * 100
        
        return self._lc_

    def _ls(self):

        """ Private method used to calculate the Liquidez Seca index. """
    
        x1 = self.data.loc[utils.cds[2], self.listofyears]
        x2 = self.data.loc[utils.cds[4], self.listofyears]
        x3 = self.data.loc[utils.cds[7], self.listofyears]
        
        self._ls_ = ( (x1-x2) / x3) * 100
        
        return self._ls_
    
    
    # Prazos Médios
    
    def _pmrv(self):
        
        """ Private method used to calculate the Prazo Médio de Recebimento de Vendas index. """
    
        x1 = self.data.loc[utils.cds[3], self.listofyears]
        x2 = self.data.loc[utils.cds[11], self.listofyears] / 360
        
        self._pmrv_ = x1 / x2

        return self._pmrv_
    
    def _pmpc(self):
        
        """ Private method used to calculate the Prazo Médio de Pagamento de Contas index. """
    
        x1 = self.data.loc[utils.cds[8], self.listofyears]
        x2 = self.data.loc[utils.cds[12], self.listofyears] * -1
        x3 = self.data.loc[utils.cds[4], self.listofyears]
        c1 = self.data.loc[utils.cds[4], self.listofyears].shift(-1)
        
        self._pmpc_ = x1 / ( (x2-c1+x3)  / 360 )
        
        return self._pmpc_

    def _pmre(self):
        
        """ Private method used to calculate the Prazo Médio de Renovação dos Estoques index. """
    
        x1 = self.data.loc[utils.cds[4], self.listofyears]
        x2 = self.data.loc[utils.cds[12], self.listofyears] * -1
        
        self._pmre_ = x1 / (x2 / 360)
        
        return self._pmre_

    def _ge(self):
        
        """ Private method used to calculate the Giro do Estoque index. """

        self._ge_ = 360 / self._pmre()

        return self._ge_
    
    
    # Rentabilidade
    
    def _ga(self):
        
        """ Private method used to calculate the Giro do Ativo index. """
    
        x1 = self.data.loc[utils.cds[11], self.listofyears]
        x2 = self.data.loc['1', self.listofyears]
        
        self._ga_ = ( x1 / x2 ) * 100
        
        return self._ga_

    def _ml(self):
        
        """ Private method used to calculate the Margem Líquida index. """
    
        x1 = self.data.loc[utils.cds[13], self.listofyears]
        x2 = self.data.loc[utils.cds[11], self.listofyears]
        self._ml_ = ( x1 / x2 ) * 100
                
        return self._ml_

    def _roa(self):
        
        """ Private method used to calculate the Rentabilidade do Ativo (ROA) index. """
    
        x1 = self.data.loc[utils.cds[13], self.listofyears]
        x2 = self.data.loc[utils.cds[0], self.listofyears]
        self._roa_ = ( x1 / x2 ) * 100

        
        return self._roa_

    def _roe(self):
        
        """ Private method used to calculate the Rentabilidade do Patrimônio Líquido (ROE) index. """
    
        x1 = self.data.loc[utils.cds[3], self.listofyears]
        x2 = self.data.loc[utils.cds[10], self.listofyears]
        c1 = self.data.loc[utils.cds[10], self.listofyears].shift(-1)
        
        self._roe_ = ( x1 / ( (x2 + c1) / 2 ) ) * 100
       
        return self._roe_

      
    
     
class Indicadores(_Indicadores):
    
    
    """ Class used to aggregate the indexes into four categories.
    
    This class inherths all attributes and methods from the parent _Indicadores and grandparent Extractor classes.
    """
    
    
    def __init__(self, filepath, s, e, anos):
        
        """ Initializes the class. """
      
        super().__init__(filepath, s, e, anos)
                          
        
    

    def _to_df(self, idx, val):
        
        """ Helper method. 
        
        This helper method aggregates individual indexes in a DataFrame.
        """
        
        df = pd.DataFrame(data = val, index = idx, columns = self.listofyears)
         
        return df

        
                    
    def estrutura_de_capital(self):
        
        """ Method. 
        
        This method calculates and aggregates the indexes of the Estruturaa de Capital category in a pd.DataFrame.
        """
        
        idx = utils.e_cap
    

        data = self._to_df( idx = idx, val = [self._pct(),
                                              self._ce(),
                                              self._ipl(),
                                              self._ccp(),
                                              self._ccl(),
                                              self._irnc()] )

        
        return data
        
    
    def liquidez(self):
        
        """ Method. 
        
        This method calculates and aggregates the indexes of the Liquidez category in a pd.DataFrame.
        """
        
        idx = utils.liq
        
        data = self._to_df( idx = idx, val = [self._lg(),
                                              self._lc(),
                                              self._ls()] )
        
        return data

    def prazos_medios(self):
        
        """ Method. 
        
        This method calculates and aggregates the indexes of the Prazos Médios category in a pd.DataFrame.
        """
        
        idx = utils.p_med

        data = self._to_df (idx = idx, val = [self._pmrv(),
                                              self._pmpc(),
                                              self._pmre(),
                                              self._ge()])
         
        return data

        
    
    def rentabilidade(self):
        
        """ Method. 
        
        This method calculates and aggregates the indexes of the Rentabilidade category in a pd.DataFrame.
        """
        
        idx = utils.rent


        data = self._to_df(idx = idx, val = [self._ga(),
                                             self._ml(),
                                             self._roa(),
                                             self._roe()])
        
        return data

    

    def todos(self):
        
        """ Method. 
        
        This method calculates and aggregates all the indexes in a pd.DataFrame.
        """
        
        est = self.estrutura_de_capital()
        liq = self.liquidez()
        prm = self.prazos_medios()
        rent = self.rentabilidade()
        
        data = pd.concat([est, liq, prm, rent], axis = 0)
        
        return data