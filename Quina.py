import numpy as np

from Verify import imprimir_jogos_destacando, imprimir_lista_verde, quantidade_numeros_sorteados, render

vetor_80 = np.arange(1, 81)
vetores_de_5 = []

while len(vetor_80) > 0:
    numeros_escolhidos = np.random.choice(vetor_80, size=5, replace=False)
    vetores_de_5.append(numeros_escolhidos)
    vetor_80 = np.setdiff1d(vetor_80, numeros_escolhidos)

def Main():
    for i, vetor in enumerate(vetores_de_5):
        print(f"'Jogo {i + 1}': {sorted(vetor)},")

        
def verify():
    game_win =[4,8,34,59,75]
    d = {'Jogo 1': [8, 10, 66, 71, 80],  
'Jogo 2': [28, 35, 72, 74, 75], 
'Jogo 3': [19, 24, 47, 51, 73], 
'Jogo 4': [2, 4, 14, 23, 43],   
'Jogo 5': [5, 7, 15, 38, 56],   
'Jogo 6': [26, 27, 60, 63, 70], 
'Jogo 7': [36, 40, 42, 53, 59], 
'Jogo 8': [33, 39, 44, 49, 77], 
'Jogo 9': [46, 52, 57, 67, 68], 
'Jogo 10': [17, 29, 32, 45, 62],
'Jogo 11': [12, 22, 41, 54, 55],
'Jogo 12': [16, 21, 30, 65, 78],
'Jogo 13': [3, 13, 18, 25, 48], 
'Jogo 14': [9, 20, 50, 58, 76],
'Jogo 15': [11, 37, 61, 64, 79],
'Jogo 16': [1, 6, 31, 34, 69],}
    _res = quantidade_numeros_sorteados(d, game_win)
    imprimir_lista_verde(sorted(game_win))
    imprimir_jogos_destacando(d, game_win)
    #render(_res)

def Run():
    res = input('-- ')
    if res == 'g':
        Main()
    if res == 'v':
        verify()
Run()