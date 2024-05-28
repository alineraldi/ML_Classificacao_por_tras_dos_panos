# -*- coding: utf-8 -*-
"""Aula 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ra4_24fB6tb9KZVSzb5XA757BrwcCLOY

Importando dados
"""

import pandas as pd

dados = pd.read_csv("/content/telecom_dados.csv")

dados.shape

dados.head()

"""Processando os dados"""

# criando dicionario
traducao_dic = {"Sim":1,
                "Nao":0}

dadosmodificados = dados[["Conjuge", "Dependentes", "TelefoneFixo", "PagamentoOnline", "Churn"]].replace(traducao_dic)
dadosmodificados.head()

#transformacao pelo get dummies
dummie_dados = pd.get_dummies(dados.drop(["Conjuge", "Dependentes", "TelefoneFixo", "PagamentoOnline", "Churn"], axis=1))

#junção dos dados modificados com os que já tinhamos
dados_final = pd.concat([dadosmodificados, dummie_dados], axis=1)
dados_final.head()

"""Definição formal

X = inputs Y = outputs
"""

# Mostrar todas as colunas
pd.set_option("display.max_columns", 39)

dados_final.head()

"""O Y é o resultado de uma função desconhecida aplicada ao X."""

Xmaria = [[0,0,1,1,0,0,39.90,1,0,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1]]

#ymaria (churn) = ?

"""Lidando com dados desbalanceados"""

# Commented out IPython magic to ensure Python compatibility.
import seaborn as sns
# %matplotlib inline

ax = sns.countplot(x='Churn', data=dados_final)

# Para podermos aplicar o SMOTE, devemos separar  os dados em variáveis características e resposta

X = dados_final.drop('Churn', axis = 1)
y = dados_final['Churn']

from imblearn.over_sampling import SMOTE

smt = SMOTE(random_state=123)  # Instancia um objeto da classe SMOTE
X, y = smt.fit_resample(X, y)  # Realiza a reamostragem do conjunto de dados

dados_final = pd.concat([X, y], axis=1)  # Concatena a variável target (y) com as features (X)

# Verifica se o balanceamento e a concatenação estão corretos.
dados_final.head(2)

ax = sns.countplot(x='Churn', data=dados_final)  # plotando a variável target balanceada.

## Caso exista um grande desbalanceamento de dados, a máquina pode acabar caindo pelo viés de prever sempre a classe majoritária.