import random
import numpy as np


from Verify import (imprimir_jogos_destacando, imprimir_lista_verde,
                    quantidade_numeros_sorteados, render)


aux_vet = []
vetores_de_6 = []
vetor_60 = [2, 3, 6, 12, 13, 14,
            20, 24, 26, 34, 35, 37,
            40, 45, 46]
#for i in range(50): vetor_60.append(1+i)
no_number = []


while len(vetor_60) < 18:
     current = random.choice(vetor_60)
     vetor_60.append(current)


if no_number:
        for i in no_number:
            vetor_60.remove(i)
else:  
    for _ in range(0):
            num = random.choice(vetor_60)
            vetor_60.remove(num)
            no_number.append(num)


while len(vetor_60) > 0:
    try:
        numeros_escolhidos = np.random.choice(vetor_60, size=6, replace=False)
        vetores_de_6.append(numeros_escolhidos)

        if len(aux_vet) < 3: aux_vet = numeros_escolhidos[4:]

        vetor_60 = np.setdiff1d(vetor_60, numeros_escolhidos)
    except:
         lis = aux_vet + vetor_60
         vetores_de_6 = lis


def Main():
   # print(sorted(no_number))
    for i, vetor in enumerate(vetores_de_6):
        print(f"{i + 1}: {sorted(vetor)},")

def verify():
    d = {}

    game_win = [6, 15, 18, 31, 32, 47]

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