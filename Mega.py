import random
import numpy as np

from Verify import imprimir_jogos_destacando, imprimir_lista_verde, quantidade_numeros_sorteados, render

vetores_de_6 = []
vetor_60 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
       31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
no_number = []

for i in range(30):
    num = random.choice(vetor_60)
    vetor_60.remove(num)
    no_number.append(num)

while len(vetor_60) > 0:
    numeros_escolhidos = np.random.choice(vetor_60, size=6, replace=False)
    vetores_de_6.append(numeros_escolhidos)
    vetor_60 = np.setdiff1d(vetor_60, numeros_escolhidos)

def Main():
    print(sorted(no_number))
    for i, vetor in enumerate(vetores_de_6):
        print(f"'Jogo {i + 1}': {sorted(vetor)},")

        
def verify():
    game_win =[]
    d = {}
    _res = quantidade_numeros_sorteados(d, game_win)
    imprimir_lista_verde(sorted(game_win))
    imprimir_jogos_destacando(d, game_win)
    
    render(_res)

Main()
#verify()