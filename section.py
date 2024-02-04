import pandas as pd
import random
from Game import countRepeatedNumbersDic, printDic

sec_1 = [1,2,3,4,5]
sec_2 = [6,7,8,9,10]
sec_3 = [11,12,13,14,15]
sec_4 = [16,17,18,19,20]
sec_5 = [21,22,23,24,25]

anotherComb = {1: [3, 1, 4, 2, 5], #formações com uma vitória
2: [3, 4, 2, 5, 1],
3: [3, 3, 3, 4, 2],
4: [3, 2, 3, 4, 3],
5: [3, 3, 2, 3, 4],
6: [1, 4, 4, 2, 4],
7: [4, 4, 1, 4, 2],
8: [4, 1, 4, 2, 4],
9: [4, 4, 2, 3, 2],
10: [2, 3, 4, 4, 2]
}
comb_dict = {1: [4, 4, 2, 3, 2], #formações com zero apostas vencidas
 2: [2, 4, 3, 2, 4],
 3: [4, 2, 2, 3, 4],
 4: [4, 4, 3, 2, 2],
 5: [2, 3, 4, 2, 4],
 6: [3, 2, 2, 4, 4],
 7: [3, 2, 3, 4, 3],
 8: [3, 3, 4, 2, 3],
 9: [3, 2, 3, 4, 3],
 10: [2, 3, 5, 2, 3]}

def extractFile(line1,line2): #Extrair os Jogos do arquivo oficial
    dicExtracted = {}
    file = r'C:\Users\Lukas\OneDrive\Documentos\Lotofácil.xlsx'
    df = pd.read_excel(file, header=None)
    intervalo_celulas = df.iloc[line1:line2,2:17]

    for i, row in enumerate(intervalo_celulas.values.tolist(), start=1):
        dicExtracted[f'{i}'] = row
    return dicExtracted

def createSecGame(lis): #Cria a formação do jogo informado no parâmetro
    secs = [sec_1,sec_2,sec_3,sec_4,sec_5]

    lisNumber = []
    for index in secs:
        contAux = 0
        for num in index:
            if num in lis:
                contAux+=1
        lisNumber.append(contAux)
    return lisNumber

def showSec(line1, line2): #Mostra Formação de todos os jogos selecionados a partir do extractFile
    dic = extractFile(line1,line2)
    for i in dic:
        aux = dic[i]
        print(f"{i} : {createSecGame(aux)}")

def createGame(lis): #Cria um jogo a partir da formação dada por uma LISTA
    listas = [sec_1, sec_2, sec_3, sec_4, sec_5]
    elementos_selecionados = []

    for i, quantidade in enumerate(lis):
        elementos_selecionados.extend(random.sample(listas[i], quantidade))
    return sorted(elementos_selecionados)

def generate(dic): #Gera sequência de jogos seguindo cada padrão presente em um DICONÁRIO de formações
    dicGames = {}
    for key,value in dic.items():
        currentFormat = value
        dicGames[key] = createGame(currentFormat)
    return dicGames

dados = {
    1:[1,	2,	3,	4,	5,	6,	8,	9,	10,	13,	17,	21,	23,	24,	25,],
    2:[1,	2,	3,	4,	5,	6,	8,	9,	10,	11,	15,	17,	20,	21,	24,],
    3:[1,	2,	5,	7,	8,	9,	11,	12,	13,	14,	15,	20,	21,	24,	25,],
    4:[1,	2,	4,	5,	6,	7,	11,	12,	13,	15,	17,	18,	20,	21,	24,],
    5:[5,	6,	7,	8,	10,	13,	14,	15,	17,	18,	19,	20,	21,	22,	25,],
    6:[1,	2,	4,	5,	7,	8,	9,	10,	11,	15,	17,	19,	20,	21,	24,],
    7:[4,	6,	7,	8,	10,	11,	12,	13,	14,	18,	20,	22,	23,	24,	25,],
    8:[1,	3,	7,	8,	10,	11,	12,	14,	15,	16,	17,	18,	19,	23,	24,],
    9:[1,	3,	4,	6,	7,	8,	11,	12,	13,	17,	18,	19,	20,	22,	23,],
    10:[1,	2,	3,	4,	6,	7,	8,	9,	14,	17,	18,	19,	20,	22,	25,],
    11:[2,	3,	4,	10,	11,	12,	14,	15,	16,	20,	21,	22,	23,	24,	25,],
    12:[1,	2,	4,	6,	8,	9,	10,	11,	14,	16,	17,	18,	19,	20,	25,],
    13:[5,	8,	11,	12,	13,	14,	15,	16,	17,	18,	20,	21,	22,	23,	24,],
    14:[1,	2,	4,	7,	8,	12,	14,	15,	16,	17,	19,	20,	21,	24,	25,],
    15:[2,	3,	4,	5,	7,	11,	12,	14,	15,	18,	19,	21,	22,	24,	25,],
    16:[1,	3,	4,	6,	7,	8,	11,	12,	13,	14,	15,	16,	17,	18,	20,],
    17:[1,	2,	4,	11,	12,	13,	15,	16,	18,	19,	20,	22,	23,	24,	25,],
    18:[1,	2,	3,	4,	5,	6,	9,	11,	12,	13,	14,	16,	22,	23,	25,],
    19:[1,	4,	5,	6,	8,	9,	12,	14,	17,	18,	19,	21,	22,	23,	25,],
    20:[1,	2,	3,	4,	5,	7,	8,	12,	13,	15,	16,	18,	19,	24,	25,],
}
printDic(generate(comb_dict))
#printDic(extractFile(3000,3011))
#for i in range(len(dados)):
#    print(f"{i+1}: {createSecGame(dados[i+1])}")
