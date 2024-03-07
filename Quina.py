import random
import numpy as np

from Verify import imprimir_jogos_destacando, imprimir_lista_verde, quantidade_numeros_sorteados, render

vetor_50 = [5,7,8,12,13,18,
            22,23,25,28,32,33,
            37,38,40,41,46,47]
            # 47 50 13 34 11 25 

vet_aux = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
vetores_de_5 = []
no_number = []

if no_number:
        for i in no_number:
            vetor_50.remove(i)
else:  
    for _ in range(0):
            num = random.choice(vetor_50)
            vetor_50.remove(num)
            no_number.append(num)


while len(vetor_50) > 0:
    numeros_escolhidos = np.random.choice(vetor_50, size=6, replace=False)
    vetores_de_5.append(numeros_escolhidos)
    vetor_50 = np.setdiff1d(vetor_50, numeros_escolhidos)

def Main():
    for i, vetor in enumerate(vetores_de_5):
        print(f"{i+1}: {sorted(vetor)},")
     
def verify():
    game_win =[13,21,39,55,67]
    d = {}
    _res = quantidade_numeros_sorteados(d, game_win)
    imprimir_lista_verde(sorted(game_win))
    imprimir_jogos_destacando(d, game_win)
    #render(_res)

def Run():
    res = input('-- ')
    if res == '1':
        print(sorted(no_number),'\n')
        Main()
    if res == '2':
        verify()
Run()