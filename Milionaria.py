import random
import numpy as np

from Verify import imprimir_jogos_destacando, imprimir_lista_verde, quantidade_numeros_sorteados, render

vetores_de_6 = []
vetor_60 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
       11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
       31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
       41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
no_number = []
    
if no_number:
        for i in no_number:
            vetor_60.remove(i)
else:  
    for _ in range(38):
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
    game_win =[10,17,26,34,43,51]
    d = {1: [10, 17, 24, 27, 51, 55],
         2: [6, 26, 34, 38, 43, 57],
         3: [10, 34, 43, 51, 55, 57],
         4: [6, 17, 24, 26, 27, 38],}
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