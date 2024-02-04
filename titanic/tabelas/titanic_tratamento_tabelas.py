import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import copy

# criando DataFrame dos arquivos csv
prevista = pd.read_csv('prevista.csv')
historica = pd.read_csv('historica.csv')


# copiando o arquivo para a variavel prev
prev = copy.deepcopy(prevista)

# copiando o arquivo para a variavel hist
hist = copy.deepcopy(historica)

# criando a coluna Survived
prev['Survived'] = 0


# adequando o DataFrame com o modelo historica.csv
prev = prev[['PassengerId',
             'Survived',
             'Pclass',
             'Name',
             'Sex',
             'Age',
             'SibSp',
             'Parch',
             'Ticket',
             'Fare',
             'Cabin',
             'Embarked']]

# encontrando só o sexo masculino no DataFrame
masc = prev['Sex'] == 'male'

# separando só os dados que contenha 'male' na coluna 'Sex
idade_masc = prev[masc]

# contando a média da idade onde a coluna 'Sex' contém 'male'
media_masc = idade_masc['Age'].mean()

# ajustando o float da media da idade masculina para duas casas decimais
media_masc = round(media_masc, 2)

# atualizando o DataFrame com as colunas idade masculina atualizadas
prev.loc[masc, 'Age'] = prev.loc[masc, 'Age'].fillna(media_masc)

# encontrando só o sexo feminino no DataFrame
fem = prev['Sex'] == 'female'

# separando só os dados que contenha 'male' na coluna 'Sex
idade_fem = prev[fem]

# contando a média da idade onde a coluna 'Sex' contém 'male'
media_fem = idade_fem['Age'].mean()
# ajustando o float da media da idade feminina para duas casas decimais
media_fem = round(media_fem, 2)

# atualizando o DataFrame com as colunas idade feminina atualizadas
prev.loc[fem, 'Age'] = prev.loc[fem, 'Age'].fillna(media_fem)


#                           Implantação da Regressão logística
# g(x) = -1.33+2.55 * ('feminino') + 1.27 * ('2ª Classe') + 2.58 * (1ª classe) - 0.04 * (Idade)


# cria a coluna isfemale
prev['isfemale'] = 0

# cria coluna isfirst
prev['isfirst'] = 0

# cria coluna issecond
prev['issecond'] = 0

# Se o 'Sex' é igual a 'female', 'isfemale' recebe 1
prev.loc[prev['Sex'] == 'female','isfemale'] = 1

# Se o 'Pclass' é igual a 1, 'isfirst'recebe 1
prev.loc[prev['Pclass'] == 1,'isfirst'] = 1

# Se o 'Pclass" é igual a 2, 'issecond'recebe 1
prev.loc[prev['Pclass'] == 2,'issecond'] = 1


# preenchendo a coluna 'Survived' com o calculo da regressao logistica
prev['Survived'] = round( -1.33+2.55 * (prev['isfemale']) + 1.27 *(prev['issecond']) + 2.58 * (prev['isfirst']) - 0.04 * (prev['Age']), 2)


# deletando as colunas de suporte
prev = prev.drop('isfemale', axis=1)
prev = prev.drop('isfirst', axis=1)
prev = prev.drop('issecond', axis=1)


# alterar os valores da coluna 'Survived' de: se maior ou igual a 1, o valor  e 2, senão, o valor e 3
# 2 == sobreviveria
# 3 == morreria
prev['Survived'] = prev['Survived'].apply(lambda i: 2 if i >=1 else 3)


# copia o DataFrame tratado para um novo DataFrame
pdf = copy.deepcopy(prev)

# concatena o DataFrame 'historica' com o DataFrame 'prevista'
pdf = pd.concat([hist,prev])


# exporta o novo DataFrame como .csv, concatenado em um novo arquivo
pdf.to_csv('historica_prevista.csv', index=False)