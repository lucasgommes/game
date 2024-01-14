import numpy as np

from Verify import imprimir_jogos_destacando, imprimir_lista_verde, quantidade_numeros_sorteados, render

vetor_60 = np.arange(1, 61)
vetores_de_6 = []

while len(vetor_60) > 0:
    numeros_escolhidos = np.random.choice(vetor_60, size=6, replace=False)
    vetores_de_6.append(numeros_escolhidos)
    vetor_60 = np.setdiff1d(vetor_60, numeros_escolhidos)

def Main():
    for i, vetor in enumerate(vetores_de_6):
        print(f"'Jogo {i + 1}': {sorted(vetor)},")
#4 - 11 - 23 - 38 - 46 - 56
        
def verify():
    game_win =[24,56,33,48,21,41]
    d = {'Jogo 1': [16, 24, 25, 29, 39, 43],
'Jogo 2': [8, 13, 14, 19, 26, 46],
'Jogo 3': [2, 15, 21, 28, 44, 58],
'Jogo 4': [9, 11, 22, 45, 57, 59],
'Jogo 5': [10, 23, 35, 38, 41, 56],
'Jogo 6': [1, 3, 5, 36, 54, 55],
'Jogo 7': [17, 20, 47, 49, 52, 53],
'Jogo 8': [6, 7, 30, 33, 37, 60],
'Jogo 9': [18, 31, 32, 34, 42, 48],
'Jogo 10': [4, 12, 27, 40, 50, 51],}
    _res = quantidade_numeros_sorteados(d, game_win)
    imprimir_lista_verde(sorted(game_win))
    imprimir_jogos_destacando(d, game_win)
    
    render(_res)

#Main()
verify()