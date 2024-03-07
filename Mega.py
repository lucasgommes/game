import random
import numpy as np

from Verify import imprimir_jogos_destacando, imprimir_lista_verde, quantidade_numeros_sorteados, render

vetores_de_6 = [] #[8,17,36,40,47,48]
vetor_60 = [4,6,8,9,18,17,
            13,22,23,28,31,33,
            34,36,40,46,47,48]
no_number = []
    
if no_number:
        for i in no_number:
            vetor_60.remove(i)
else:  
    for _ in range(0):
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
        print(f"{i + 1}: {sorted(vetor)},")

def verify():
    d = {1: [9, 28, 33, 36, 46, 47],
            2: [6, 13, 18, 22, 34, 48],
            3: [4, 8, 17, 23, 31, 40],
            
            1: [6, 22, 31, 33, 34, 40],
            2: [4, 8, 17, 18, 23, 28],
            3: [9, 13, 36, 46, 47, 48],
}

    game_win = [8,17,36,40,47,48]

    _res = quantidade_numeros_sorteados(d, game_win)
    imprimir_lista_verde(sorted(game_win))
    imprimir_jogos_destacando(d, game_win)
    
    render(_res)

def run():
    answ = input('1: Main\n2: Verify\n--')
    if answ == '1':
        Main()
    if answ == '2':
        verify()

run()