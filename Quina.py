import random
import numpy as np

from Verify import imprimir_jogos_destacando, imprimir_lista_verde, quantidade_numeros_sorteados, render

vetor_50 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
            71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
            

vet_aux = []
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
    numeros_escolhidos = np.random.choice(vetor_50, size=5, replace=False)
    vetores_de_5.append(numeros_escolhidos)
    vetor_50 = np.setdiff1d(vetor_50, numeros_escolhidos)

def Main():
    for i, vetor in enumerate(vetores_de_5):
        print(f"{i+1}: {sorted(vetor)},")
     
def verify():
    game_win =[6,7,12,23,51]
    d = {1: [13, 25, 49, 72, 78],
2: [24, 36, 47, 53, 70],
3: [15, 29, 41, 56, 60],
4: [7, 59, 69, 74, 80],
5: [3, 10, 54, 57, 79],
6: [26, 43, 44, 45, 68],
7: [17, 27, 63, 65, 76],
8: [11, 12, 20, 32, 52],
9: [2, 22, 34, 61, 64],
10: [4, 37, 46, 48, 75],
12: [5, 30, 31, 38, 58]}
#11: [6, 9, 18, 28, 66]
#13: [8, 21, 39, 50, 62],
#14: [35, 40, 51, 67, 71],
#15: [1, 23, 33, 42, 55],
#16: [14, 16, 19, 73, 77],
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