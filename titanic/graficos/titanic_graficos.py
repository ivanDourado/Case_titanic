import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import copy

#  criando o DataFrame do arquivo .csv
histprev_df = pd.read_csv('historica_prevista.csv')


# •	Um gráfico (semelhante ao abaixo) apresentando o percentual de pessoas embarcadas em cada porto
#  (local de embarque)

def embarcados():
    # separando a coluna 'Embarked' em uma variável, contando a porcentagem de cada tipo de embarcado,
    #  mesmo com o valor nulo
    emb = histprev_df['Embarked'].value_counts(normalize=True, dropna=False) * 100

    # cirando o grafico de pizza, retornando as porcentagens dentro de sua respectiva fatia, e atribuindo nomes a elas
    wedges, texts, autotexts = plt.pie(emb, labels=['Southampton',
                                                    'Queenstone',
                                                    'Cherburg',
                                                    'Nao consta'
                                                    ], autopct='%1.1f%%')

    # titulo do grafico
    plt.title('Embarked Stations')

    # atribuindo nome e posicao a legenda
    plt.legend(title='Legenda', loc='upper left',
               bbox_to_anchor=(1, 0, 0.5, 1))

    # definindo a fonte e o tamanho da fonte para cada fatia
    plt.setp(autotexts, size=10)

    # plotando o grafico

    return plt.show()


# •	Um gráfico(semelhante ao abaixo) apresentando o percentual e o número de pessoas no navio por classe


def por_classe():
    # separando a coluna 'Pclass' em uma variavel, contando a porcentagem de cada tipo de classe
    clss = histprev_df['Pclass'].value_counts(normalize=True) * 100

    # criando o grafico de pizza, retornando as porcentagens dentro de sua espectiva fatia, atribuindo nomes a elas
    wedges, texts, autotexts = plt.pie(clss, labels=['3rd Class',
                                                     '1st Class',
                                                     '2nd Class',
                                                     ], autopct='%1.1f%%')

    # titulo do grafico
    plt.title('Passenger Class')

    # atribuindo nome e posicao a legenda
    plt.legend(title='Legenda', loc='upper left',
               bbox_to_anchor=(1, 0, 0.5, 1))

    # definindo a fonte e o tamanho da fonte para cada fatia
    plt.setp(autotexts, size=10)

    # plotando o grafico

    return plt.show()


# •	Um gráfico(semelhante ao abaixo) apresentando o número de irmãos / cônjuges a bordo do Navio

def sibsp():
    # separando a coluna 'Sibsp' em uma variavel, separando por grupo
    sbsp = histprev_df['SibSp'].value_counts(dropna=False)

    # determina o tamanho da plotagem
    fig, ax = plt.subplots(figsize=(8, 6))

    # determina uma cor para cada barra
    color = ['royalblue', 'orange', 'seagreen',
             'brown', 'slateblue', 'darkorange', 'orchid']

    # determina o formato da plotagem, o comprimento de cada barra, e o eixo de alinhamento
    sbsp.plot(kind='bar', ax=ax, color=(color), width=0.9, align='center')

    # determina o titulo do grafico, o do eixo x e do eixo y
    plt.title('Number of Simbling and Spouse')
    ax.set_xlabel('SibSp')
    ax.set_ylabel('Count')
    return plt.show()


# •	Um gráfico(semelhante ao abaixo) apresentando o número de pais / filhos a bordo do Navio


def pais_filhos():
    # separando a coluna 'Parch' em uma variavel, separando por grupo
    parch = histprev_df['Parch'].value_counts(dropna=False)

    # determina o tamanho da plotagem
    fig, ax = plt.subplots(figsize=(8, 6))

    # determina uma cor para cada barra
    color2 = ['royalblue', 'orange', 'seagreen',
              'brown', 'slateblue', 'darkorange', 'orchid', 'teal']

    # determina o formato da plotagem, o comprimento de cada barra, e o eixo de alinhamento
    parch.plot(kind='bar', ax=ax, color=(color2), width=0.9, align='center')

    # determina o titulo do grafico, o do eixo x e do eixo y
    plt.title('Number of parent & children')
    ax.set_xlabel('Parch')
    ax.set_ylabel('Count')
    return plt.show()


# •	Um gráfico(semelhante ao abaixo) apresentando o número de passageiros por idade (em faixas de 10 anos) e em conjunto com a média de idade dos passageiros

def idades_por_dez():
    # copio a tabela para a variavel age
    age = copy.deepcopy(histprev_df)

    # delimito cada barra a agrupar as idades por cada decada
    bins_age = range(int(age['Age'].min()), int(age['Age'].max()) + 11, 10)

    # seto a plotagem com base na variavel bins_age, e ativo a linha de densidade
    sns.histplot(data=age, x='Age', bins=bins_age, kde=True, alpha=0.8)

    # plotagem do grafico
    plt.xlabel('Age grouped by ten')
    plt.ylabel('Count')
    return plt.show()


# •	Um 2o com o número dos que sobreviveriam ou morreriam baseado nas sugestões que vocês encontraram
# •	E um 3º, com todas as possibilidades(sobreviveu, morreu, sobreviveria e morreria)

def sobrevive():
    surv = histprev_df['Survived'].value_counts(dropna=False)
    fig, ax = plt.subplots(figsize=(8, 6))

    color = ['royalblue', 'orange', 'seagreen',
             'brown']

    surv.plot(kind='bar', ax=ax, color=(color), width=0.9,
              align='center')

    plt.title('Survived or not & would survive or not')
    ax.set_xlabel('Survived or not & would survive or not')
    ax.set_ylabel('Count')
    return plt.show()


# •	Um gráfico(semelhante ao abaixo) apresentando o número de passageiros e percentual dos que sobreviveram ou não.
def sobreviveu():
    surv_hist = histprev_df['Survived']
    surv_hist_f = surv_hist.isin([0, 1])
    surv1 = histprev_df.loc[surv_hist_f]

    survg1 = surv1['Survived'].value_counts(dropna=False)

    fig, ax = plt.subplots(figsize=(8, 6))

    color = ['royalblue', 'orange']

    survg1.plot(kind='bar', ax=ax, color=(color), width=0.9,
                align='center')

    plt.title('Survived or not')
    ax.set_xlabel('Survived or not')
    ax.set_ylabel('Count')
    return plt.show()


# •	Um 2o com o número dos que sobreviveriam ou morreriam baseado nas sugestões que vocês encontraram

def sobreviveria():
    surv_prev = histprev_df['Survived']
    surv_prev_f = surv_prev.isin([2, 3])
    surv2 = histprev_df.loc[surv_prev_f]

    survg2 = surv2['Survived'].value_counts(dropna=False)

    fig, ax = plt.subplots(figsize=(8, 6))

    color = ['royalblue', 'orange']

    survg2.plot(kind='bar', ax=ax, color=(color), width=0.9,
                align='center')

    plt.title('Would survive or not')
    ax.set_xlabel('Would survive or not')
    ax.set_ylabel('Count')
    return plt.show()


# •	E um 3º, com todas as possibilidades(sobreviveu, morreu, sobreviveria e morreria)
def sobrevive_classe():
    # copio o DataFrame para um novo
    class_surv = copy.deepcopy(histprev_df)

    # separo os valores por grupo de classe e o subgrupo de sobreviventes
    pclassc = class_surv.groupby('Pclass')['Survived'].value_counts().unstack()

    # determino o tamanho do grafico
    plt.rc('figure', figsize=(10, 5))

    # determino o tipo do grafico
    pclassc.plot(kind='bar', stacked=True)

    # estilizo o grafico e a legenda
    plt.legend(('Died', 'Survived', 'Would Survived', 'Would Died'), loc='best')
    plt.title('Survived or not & Would Survived or not by Pclass')
    plt.xlabel('Classes')
    plt.ylabel('Count')
    plt.xticks(rotation=0)

    return plt.show()


def sobreviveu_classe():
    # •	Um gráfico(semelhante ao abaixo) apresentando o número de passageiros e o percentual que sobreviveram ou não por classe.
    # copio o DataFrame para um novo
    class_surv = copy.deepcopy(histprev_df)

    # separo os valores por grupo de classe e o subgrupo de sobreviventes
    pclassc = class_surv.groupby('Pclass')['Survived'].value_counts().unstack()
    # Separo apenas os resultados 0 e 1 da coluna Survived
    pclassc_hist = pclassc[[1, 0]]

    # determino o tamanho do gráfico
    plt.rc('figure', figsize=(10, 5))

    # determino o tipo do grafico
    pclassc_hist.plot(kind='bar', stacked=True)

    # estilizo o grafico e a legenda
    plt.legend(('Survived', 'Died'), loc='best')
    plt.title('Survived or not by Pclass')
    plt.xlabel('Classes')
    plt.ylabel('Count')
    plt.xticks(rotation=0)

    return plt.show()


def sobreviveria_classe():
    # •	Um 2o com o número dos que sobreviveriam ou morreriam baseado nas sugestões que vocês encontraram
    # copio o DataFrame para um novo
    class_surv = copy.deepcopy(histprev_df)

    # separo os valores por grupo de classe e o subgrupo de sobreviventes
    pclassc = class_surv.groupby('Pclass')['Survived'].value_counts().unstack()
    # Separo apenas os resultados 3 e 2 da coluna Survived
    pclassc_prev = pclassc[[3, 2]]

    # determino o tamanho do gráfico
    plt.rc('figure', figsize=(10, 5))

    # determino o tipo do grafico
    pclassc_prev.plot(kind='bar', stacked=True)

    # estilizo o grafico e a legenda
    plt.legend(('Would Survived', 'Would Died'), loc='best')
    plt.title('Would Survived or not by Pclass')
    plt.xlabel('Classes')
    plt.ylabel('Count')
    plt.xticks(rotation=0)

    return plt.show()


# •	E um 3º, com todas as possibilidades(sobreviveu, morreu, sobreviveria e morreria)
def sobrevive_sexo():
    # copio o DataFrame para  um novo
    sex_surv = copy.deepcopy(histprev_df)

    # separo os valores por grupo de sexo e o subgrupo de sobreviventes
    sexc = sex_surv.groupby('Sex')['Survived'].value_counts().unstack()

    # determino o tamanho do grafico
    plt.rc('figure', figsize=(10, 5))

    # determino o tipo do grafico
    sexc.plot(kind='bar', stacked=True)

    # estilizo o grafico e a legenda
    plt.legend(('Died', 'Survived', 'Would Died', 'Would Survived'), loc='best')
    plt.title('Survived or not & Would Survived or not by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.xticks(rotation=0)

    return plt.show()


# Um gráfico(semelhante ao abaixo) apresentando o número de passageiros e percentual que sobreviveram ou não por sexo.
def sobreviveu_sexo():
    # copio o DataFrame para um novo
    sex_surv = copy.deepcopy(histprev_df)

    # separo os valores por grupo de sexo e o subgrupo de sobreviventes
    sexc = sex_surv.groupby('Sex')['Survived'].value_counts().unstack()

    # Separo apenas os resultados 1 e 0 da coluna Survived
    sexc_hist = sexc[[1, 0]]

    # determino o tamanho do grafico
    plt.rc('figure', figsize=(10, 5))

    # determino o tipo do grafico
    sexc_hist.plot(kind='bar', stacked=True)

    # estilizo o grafico e a legenda
    plt.legend(('Would Survived', 'Would Died'), loc='best')
    plt.title('Would Survived or not by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.xticks(rotation=0)

    return plt.show()


# •	Um 2o com o número dos que sobreviveriam ou morreriam baseado nas sugestões que vocês encontraram
def sobreviveria_sexo():
    # copio o DataFrame para  um novo
    sex_surv = copy.deepcopy(histprev_df)

    # separo os valores por grupo de sexo e o subgrupo de sobreviventes
    sexc = sex_surv.groupby('Sex')['Survived'].value_counts().unstack()
    # Separo apenas os resultados 3 e 2 da coluna Survived
    sexc_prev = sexc[[3, 2]]

    # determino o tamanho do grafico
    plt.rc('figure', figsize=(10, 5))

    # determino o tipo do grafico
    sexc_prev.plot(kind='bar', stacked=True)

    # estilizo o grafico e a legenda
    plt.legend(('Would Survived', 'Would Died'), loc='best')
    plt.title('Would Survived or not by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.xticks(rotation=0)

    return plt.show()


def opt():
    valid = False
    while not valid:
        try:
            opcao = int(input('Digite a sua opção:\n'))
            if 1 <= opcao <= 9:
                valid = True
                return opcao
            else:
                print('Favor escolher entre uma das opções')
        except ValueError:
            print('Use apenas os números das opções')


def menu(value):

    valid = False

    while not valid:
        if value == 1:
            embarcados()
            menu(opt())
        if value == 2:
            por_classe()
            menu(opt())
        if value == 3:
            sibsp()
            menu(opt())
        if value == 4:
            pais_filhos()
            menu(opt())
        if value == 5:
            idades_por_dez()
            menu(opt())
        if value == 6:
            print('1- Todos passageiros que sobreviveram e sobreviveriam\n'
                  '2- Todos passageiros que sobreviveram ou não\n'
                  '3- Todos passageiros que sobreviveriam ou não\n'
                  '4- Voltar ao menu anterior')
            submenu1(sub_opt())

        if value == 7:
            print('1- Todos passageiros que sobreviveram e sobreviveriam, por classe\n'
                  '2- Todos passageiros que sobreviveram ou não, por classe\n'
                  '3- Todos passageiros que sobreviveriam ou não, por classe\n'
                  '4- Voltar ao menu anterior')
            submenu2(sub_opt())

        if value == 8:
            print('1- Todos passageiros que sobreviveram e sobreviveriam, por sexo\n'
                  '2- Todos passageiros que sobreviveram ou não, por sexo\n'
                  '3- Todos passageiros que sobreviveriam ou não, por sexo\n'
                  '4- Voltar ao menu anterior')
            submenu3(sub_opt())

        if value == 9:
            print('Até mais')
            valid = True


def sub_opt():
    valid = False
    while not valid:
        try:
            opcao = int(input('Digite a sua opção:\n'))
            if 1 <= opcao <= 3:
                valid = True
                return opcao
            else:
                print('Favor escolher entre uma das opções')
        except ValueError:
            print('Use apenas os números das opções')


def submenu1(value):

    if value == 1:
        sobrevive()
        submenu1(opt())
    if value == 2:
        sobreviveu()
        submenu1(opt())
    if value == 3:
        sobreviveria()
        submenu1(opt())
    if value == 4:
        print('1- para ver quantos embarcaram em cada porto\n'
              '2- Para ver quantos entraram de cada classe\n'
              '3- Para ver quantos eram irmãos e cônjuges\n'
              '4- Para ver quantos eram Pais e Filhos\n'
              '5- Passageiros por idade(de dez em dez)\n'
              '6- Todos passageiros que sobreviveram e sobreviveriam\n'
              '7- Todos passageiros que sobreviveram e sobreviveriam, por classe\n'
              '8- Todos passageiros que sobreviveram e sobreviveriam, por sexo\n'
              '9- Sair')
        menu(opt())


def submenu2(value):

    if value == 1:
        sobrevive_classe()
        submenu1(opt())
    if value == 2:
        sobreviveu_classe()
        submenu1(opt())
    if value == 3:
        sobreviveria_classe()
        submenu1(opt())
    if value == 4:
        print('1- para ver quantos embarcaram em cada porto\n'
              '2- Para ver quantos entraram de cada classe\n'
              '3- Para ver quantos eram irmãos e cônjuges\n'
              '4- Para ver quantos eram Pais e Filhos\n'
              '5- Passageiros por idade(de dez em dez)\n'
              '6- Todos passageiros que sobreviveram e sobreviveriam\n'
              '7- Todos passageiros que sobreviveram e sobreviveriam, por classe\n'
              '8- Todos passageiros que sobreviveram e sobreviveriam, por sexo\n'
              '9- Sair')
        menu(opt())


def submenu3(value):

    if value == 1:
        sobrevive_sexo()
        submenu1(opt())
    if value == 2:
        sobreviveu_sexo()
        submenu1(opt())
    if value == 3:
        sobreviveria_sexo()
        submenu1(opt())
    if value == 4:
        print('1- para ver quantos embarcaram em cada porto\n'
              '2- Para ver quantos entraram de cada classe\n'
              '3- Para ver quantos eram irmãos e cônjuges\n'
              '4- Para ver quantos eram Pais e Filhos\n'
              '5- Passageiros por idade(de dez em dez)\n'
              '6- Todos passageiros que sobreviveram e sobreviveriam\n'
              '7- Todos passageiros que sobreviveram e sobreviveriam, por classe\n'
              '8- Todos passageiros que sobreviveram e sobreviveriam, por sexo\n'
              '9- Sair')
        menu(opt())

# menu Titanic


print('Dados Caso Titanic')

print('1- para ver quantos embarcaram em cada porto\n'
      '2- Para ver quantos entraram de cada classe\n'
      '3- Para ver quantos eram irmãos e cônjuges\n'
      '4- Para ver quantos eram Pais e Filhos\n'
      '5- Passageiros por idade(de dez em dez)\n'
      '6- Todos passageiros que sobreviveram e sobreviveriam\n'
      '7- Todos passageiros que sobreviveram e sobreviveriam, por classe\n'
      '8- Todos passageiros que sobreviveram e sobreviveriam, por sexo\n'
      '9- Sair')

while menu(opt()) != 9:
    print('1- para ver quantos embarcaram em cada porto\n'
          '2- Para ver quantos entraram de cada classe\n'
          '3- Para ver quantos eram irmãos e cônjuges\n'
          '4- Para ver quantos eram Pais e Filhos\n'
          '5- Passageiros por idade(de dez em dez)\n'
          '6- Todos passageiros que sobreviveram e sobreviveriam\n'
          '7- Todos passageiros que sobreviveram e sobreviveriam, por classe\n'
          '8- Todos passageiros que sobreviveram e sobreviveriam, por sexo\n'
          '9- Sair')

    menu(opt())
