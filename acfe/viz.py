# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:46:57 2022

@author: Fernando Gioppato
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from acfe.utils import *


def kpi():
    
    kpi_dict = {'Participação de Capital de Terceiros' : 'pct', 
                'Composição do Endividamento' : 'ce',
                'Imobilização do Patrimônio Líquido' : 'ipl',
                'Capital Circulante Próprio' : 'ccp',
                'Capital Circulante Líquido' : 'ccl',
                'Imobilização de Recursos Não Correntes' : 'irnc',
                'Liquidez Geral' : 'lg',
                'Liquidez Corrente' : 'lc',
                'Liquidez Seca' : 'ls',
                'Prazo Médio de Recebimento de Vendas' : 'pmrv',
                'Prazo Médio de Pagamento de Contas' : 'pmpc', 
                'Prazo Médio de Renovação de Estoques' : 'pmre',
                'Giro do Estoque' : 'ge',
                'Giro do Ativo' : 'ga', 
                'Margem Líquida' : 'ml',
                'Rentabilidade do Ativo (ROA)' : 'roa',
                'Rentabilidade do Patrimônio Líquido (ROE)' :'roe'}
    
    return kpi_dict


def plotter():
    
    
    
    
    
    
    pass