# Análise Contábil e Financeira de Empresas

Projeto baseado na disciplina **Análise Contábil e Financeira de Empresas - Ciências Econômicas, UNESP Araraquara.**

Como avaliação da disciplina, nós deveríamos realizar uma Análise Fundamentalista de alguma empresa listada na bolsa de valores B3. A empresa é de escolha do grupo, mas o período de análise deve ser de 3 anos.

Os índices utilizados se dividiam em 4 categorias:

<details>
<summary>Estrutura de Capital</summary>
    
    - Participação de Capital de Terceiros
    
    - Composição do Endividamento
        
    - Imobilização do Patrimônio Líquido  
        
    - Capital Circulante Próprio (CCP)
        
    - Capital Circulante Líquido (CCL)
            
    - Imobilização de Recursos Não Correntes
</details>

<details>
<summary>Liquidez</summary>
    
    - Liquidez Geral
    
    - Liquidez Corrente
    
    - Liquidez Seca
</details>

<details>
<summary>Rentabilidade</summary>
    
    - Giro do Ativo
    
    - Margem Líquida
    
    - Rentabilidade do Ativo (ROA)
    
    - Rentabilidade do Patrimônio Líquido (ROE)
</details>

<details>
<summary>Prazos Médios</summary>

    - Prazo Médio de Recebimento de Vendas (PMRV)
    
    - Prazo Médio de Pagamento de Contas (PMPC)
    
    - Prazo Médio de Renovação de Estoques (PMRE)
    
    - Giro do Estoque
</details>

Na disciplina tanto os cálculos quanto a 'extração' dos dados são feitos de maneira manual, o primeiro utilizando o Excel. A proposta deste projeto é desenvolver um pacote na linguagem Python que:

1. Extraia os dados dos Demonstrativos Financeiros das empresas;
2. Realize os cálculos dos índices;
3. Plote visualizações básicas.


## Pacote
O pacote será estruturado da seguinte maneira:
```
acfe/
|-- __init__.py
|
|-- extracao.py
|
|-- indices.py
|
|-- visualizacao.py
```

### extracao.py
Contém o(s) script(s) necessário(s) para extrair os dados do arquivo `.pdf` e consolidá-los no formato de um `pd.DataFrame`.
A extração será feita por meio de expressões regulares - ***regex***.

### indices.py
Contém o script necessário para realizar o cálculo dos índices. Cada módulo é responsável pelo cálculo de uma das quatro categorias de índices, e leva o nome de sua categoria.

### visualizacao.py
Contém o script necessário para visualizar os índices.
