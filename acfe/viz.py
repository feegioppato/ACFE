# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:46:57 2022

@author: Fernando Gioppato
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from acfe import Indicadores


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


# =============================================================================
# def plot_kpi(obj, kpi):
#     
#     """
#     Plot individual KPIs
#     
#     
#     Arguments
#     ---------
#     data: Indicadores object
#         
#     kpi: strig
#         
#     """
#     
#     
#     fig, ax = plt.subplots() 
#     
#     data = 
#     
#     bars = ax.bar(data.index, data, color = '#1F77B4')
#     ax.set_title(kpi()[f'_{kpi}'], alpha = .85, fontsize = 17, loc = 'left')
# 
#     for spine in plt.gca().spines.values():
#         spine.set_visible(False)
#         ax.spines['top'].set_visible(True)
#         ax.spines['top'].set_position('zero')
# 
#     ax.tick_params(bottom = False, left = False, top = True, labelleft = False, labelbottom = False, labeltop = True)
# 
#     ax.grid(True, axis = 'y', alpha = .15)    
# 
#     for bar in bars:
#         height = bar.get_height()
#         plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1000000, str(int(height)), 
#                        ha='center', color='w', fontsize=13)
# =============================================================================
        
        
        
    
    