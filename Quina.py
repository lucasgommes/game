import random
import numpy as np

from Verify import imprimir_jogos_destacando, imprimir_lista_verde, quantidade_numeros_sorteados, render

vetor_80 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
            71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
vetores_de_5 = []
no_number = []

if no_number:
        for i in no_number:
            vetor_80.remove(i)
else:  
    for _ in range(65):
            num = random.choice(vetor_80)
            vetor_80.remove(num)
            no_number.append(num)


while len(vetor_80) > 0:
    numeros_escolhidos = np.random.choice(vetor_80, size=5, replace=False)
    vetores_de_5.append(numeros_escolhidos)
    vetor_80 = np.setdiff1d(vetor_80, numeros_escolhidos)

def Main():
    for i, vetor in enumerate(vetores_de_5):
        print(f"{i+1}: {sorted(vetor)},")
     
def verify():
    game_win =[50,52,54,56,58]
    d = {1: [16, 19, 29, 32, 78],
2: [7, 40, 46, 56, 72],
3: [27, 31, 42, 63, 76],}
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