# -*- coding: utf-8 -*-

# Impotando bibliotecas

from zipfile import ZipFile
import pandas as pd
import wget
import re
import os



# Função para realizar o download dos arquivos zip
def url_download(anos = ['2021'], diretorio = os.getcwd()):
    
    """
    Faz o download dos aqrquivos .zip para os anos selecionados. Cada arquivo contém
    todos os dados de BPA, BPP, DRE, DFC_MD, DFC_MI, DMPL e DVA de todas as empresas
    listadas na B3 naquele ano.
    
    Parameters
    ----------
    anos: list, optional
        (Default value: ['2021']))
    
    Returns
    -------
    zips: lista com nome dos arquivos .zip
    
    Arquivos .zip armazenados no diretório de trabalho.

    """
    
    url_base = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'

    zips = []

    dir_dados = f'{diretorio}/Dados'

    if not os.path.exists(dir_dados):
        os.mkdir(dir_dados)
    
    for ano in anos:
        zips.append(f'dfp_cia_aberta_{ano}.zip')


    for arq in zips:
        wget.download(url_base+arq, out = dir_dados)

    return zips   



def extractor(principais = True, balancos = ['BPA_con', 'BPP_con', 'DRE_con'], diretorio = os.getcwd()):
    
    """ 
    Extrai os arquivos .csv de dentro dos arquivos .zip e salva no diretório de trabalho.
    Cada arquivo .csv salvo contém as informações de um balanço específico (BPA, BPP, etc.)
    para o período escolhido.
    
    Parameters
    ----------
    principais: Bool, optional
        Default value: True
        
    balancos: list, optional
        Default value: ['BPA_con', 'BPP_con', 'DRE_con']
        
    diretorio: str, optional
        Default value: diretorio de trabalho atual.
        
        
    Returns
    -------
    Arquivos .csv salvos no diretório de trabalho atual.
    """
    
    
    contas = ['BPA_con', 'BPP_con', 'DFC_MD_con',
             'DFC_MI_con', 'DMPL_con', 'DRE_con', 'DVA_con']
    
    folder = []
    for arq in zips:
        folder.append(f'{os.getcwd()}/Dados/{arq}')
    
    
    if principais == True:
        
        for conta in balancos:
            demonstrativo = pd.DataFrame()
            anos = []
            
            for file in folder:
                zf = ZipFile(file)
                
                ano = re.findall(r'\d{4}', file)[0]
                
                anos.append(ano)
                
                demonstrativo = pd.concat([demonstrativo, pd.read_csv(zf.open(f'dfp_cia_aberta_{conta}_{ano}.csv'),
                                                                      sep = ';', decimal = ',', encoding = 'ISO-8859-1')])
                 
            dir_dados = f'{diretorio}\Dados'
            
            nome_arquivo = f'dfp_cia_aberta_{conta}_{anos[0]}-{anos[-1]}.csv'
            
            if not os.path.exists(dir_dados):
                os.mkdir(dir_dados)
                
            caminho = os.path.join(dir_dados, nome_arquivo)
            
            demonstrativo.to_csv(caminho, index = False)

    else:
        
        for conta in contas:
            demonstrativo = pd.DataFrame()
            anos = []
            
            for file in zips:
                zf = ZipFile(file)
                
                ano = re.findall(r'\d{4}', file)[0]
                
                anos.append(ano)
                
                demonstrativo = pd.concat([demonstrativo, pd.read_csv(zf.open(f'dfp_cia_aberta_{conta}_{ano}.csv'),
                                                                      sep = ';', decimal = ',', encoding = 'ISO-8859-1')])
                 
            dir_dados = f'{diretorio}\Dados'
            
            nome_arquivo = f'dfp_cia_aberta_{conta}_{anos[0]}-{anos[-1]}.csv'
            
            if not os.path.exists(dir_dados):
                os.mkdir(dir_dados)
                
            caminho = os.path.join(dir_dados, nome_arquivo)
            
            demonstrativo.to_csv(caminho, index = False)
            
            # demonstrativo.to_csv(diretorio + f'\Dados\dfp_cia_aberta_{conta}_{anos[0]}-{anos[-1]}.csv', index = False)




 







