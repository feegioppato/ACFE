# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:33:18 2022

@author: Fernando Gioppato
"""

import re
import os
import tika
from tika import parser
import pandas as pd

# Lendo arquivo pdf
parsed = parser.from_file(r'C:\Users\ferna\Projetos\ACFE\Dados\Demonstrativos Ambev (2017, 2018, 2019).pdf')

# Variável com o conteúdo
text = parsed['content']

# Preparando o documento para extração
# Deve ser incluida pelo usuário
p1 = 'PÁGINA: 2 de 137'
p2 = 'PÁGINA: 9 de 137'
paginas_interesse = re.search(f"(?<={p1}).*(?={p2})", text, re.DOTALL)
#paginas_interesse = re.search('(?<=PÁGINA: 2 de 137).*(?=PÁGINA: 9 de 137)', text, re.DOTALL)
dados_brutos = paginas_interesse.group(0)



# Expressão Regular para extrair dados
pattern = r'''
(?P<numero_conta>\d(?:\.\d{1,2})*)\s
(?P<nome_conta>(?:[a-zA-Zâãõçíó\-\)\(]+\s)+)
(?P<primeiro_ano>-?\d{1,3},?(?:,?\.?\d{1,3})*)*\s
(?P<segundo_ano>-?\d{1,3},?(?:,?\.?\d{1,3})*)*\s
(?P<terceiro_ano>-?\d{1,3}(?:,?\.?\d{1,3})*)'''
p = re.compile(pattern, re.X)

# Extraindo grupos de interesse
resultados = []
for linha in re.finditer(p, dados_brutos):
    resultados.append(linha.groupdict())

# Transformando saída em um dataframe
df = pd.DataFrame(resultados)





