#!/usr/bin/env python
# coding: utf-8

# # Tarefa 02 Módulo 05
# 
# O nosso projeto desta sequência de módulos do curso será um aprofundamento da demonstração sobre classificação de risco de crédito que vimos lá no comecinho. Pois recebemos uma base já montada pra nós. Tenha certeza de que ela passou por um longo processamento até ficar daquele jeito. Neste exercício vamos exercitar o que aprendemos nas ultimas aulas e montar a variável resposta da base do nosso projeto

# #### Marcação de bom e mau
# O objetivo da modelagem é classificar o risco de inadimplência, ou como se diz no meio, o risco de *default*. Podemos fazer longas discussões sobre o conceito de *default* com base em estudos e exigências regulatórias, para efeitos deste estudo, um cliente em *default* é aquele que está em 60 dias de atraso ou mais. Então classificaremos os clientes como 'bons' e 'maus' assim:
# - **Maus** pagadores: são aqueles que entraram em 'default' (atraso 60 dias ou mais) nos 24 meses seguintes à aquisição do cartão de crédito. 
# - **Bons** pagadores: são considerados todos os demais.
# - **Excluídos**: Clientes que não adquiriram um cartão de crédito (seja por recusa, seja por desistência) não possuem informações de pagamento, portanto não se pode identificar se são bons ou maus. Há uma longa discussão e literatura sobre *inferência de rejeitados* que está fora do escopo deste exercício.

# #### Bases disponíveis
# Temos duas bases importantes aqui: uma de propostas, com diversas informações dos vários solicitantes de cartão de crédito, e uma base de pagamentos. A base de pagamentos será utilizada para identificar a ocorrência de *default*. A base de propostas tem diversas informações coletadas no momento da solicitação do crédito (isto é importante: qualquer informação posterior a essa data é impossível de ser coletada na aplicação do modelo e não pode ser utilizada).

# In[ ]:


import pandas as pd

# Ler o arquivo CSV (substitua 'seu_arquivo.csv' pelo nome do seu arquivo)
arquivo_csv = 'seu_arquivo.csv'
dados_csv = pd.read_csv(arquivo_csv)

# Exibir os dados
dados_csv


# In[ ]:


import pandas as pd

# Carregando as bases de dados
propostas = pd.read_csv('caminho/do/arquivo/application_records.csv')
pagamentos = pd.read_csv('caminho/do/arquivo/pagamentos_largo.csv')


# In[ ]:


from google.colab import files

# Solicitar ao usuário para fazer o upload do arquivo
uploaded = files.upload()

# Obter o nome do arquivo
filename = list(uploaded.keys())[0]

# Carregar o arquivo CSV em um DataFrame Pandas
import pandas as pd
df = pd.read_csv(filename)

# Visualizar as primeiras linhas do DataFrame
df.head()


# In[ ]:


propostas = pd.read_csv('application_record.csv')
pg = pd.read_csv('pagamentos_largo.csv')


# In[ ]:


# Tarefa 1) Marcar default no mês
meses_default = ['mes_00', 'mes_01', 'mes_02', 'mes_03', 'mes_04', 'mes_05', 'mes_06', 'mes_07', 'mes_08', 'mes_09', 'mes_10', 'mes_11', 'mes_12', 'mes_13', 'mes_14', 'mes_15', 'mes_16', 'mes_17', 'mes_18', 'mes_19', 'mes_20', 'mes_21', 'mes_22', 'mes_23', 'mes_24']

for mes in meses_default:
    propostas[mes + '_default'] = propostas['ID'].isin(pagamentos[pagamentos[mes].isin(['1', '2', '3', '4', '5'])]['ID'])


# In[ ]:


# Tarefa 2) 'bons' e 'maus' ao longo de todos os 24 meses de desempenho
propostas['mau_pagador'] = propostas[meses_default].sum(axis=1) > 0


# In[ ]:


# Tarefa 3) Marcando proponentes expostos ao risco de crédito
propostas_expostos = propostas[propostas['ID'].isin(pagamentos['ID'])]


# In[ ]:


# Tarefa 4) Consolidando as informações
propostas_final = pd.merge(propostas_expostos, propostas_expostos[meses_default].applymap(lambda x: 1 if x else 0), left_on='ID', right_on='ID', suffixes=('', '_default'))


# In[ ]:


# Tarefa 5) Verificando
contagem_default = propostas_final['mau_pagador'].value_counts()
print(contagem_default)


# In[ ]:




