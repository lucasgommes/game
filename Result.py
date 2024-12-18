from Verify import *
from Tests.section import createSecGame



def noRepeatInList(l:list):
    auxList =[]
    for i in range(1,26):
        if i not in l:
            auxList.append(i)
    return auxList

def show_result(dic:dict, game_win):
    _res = quantidade_numeros_sorteados(dic, game_win)
    #imprimir_lista_verde(sorted(game_win))
    #print(noRepeatInList(game_win))
    #print(createSecGame(game_win))
    imprimir_jogos_destacando(dic, game_win)
    render(_res)

win = [1, 4, 5, 6, 7, 9, 10, 11, 13, 15, 16, 18, 19, 21, 23]

d = {'Número 1': [1, 4, 5, 7, 9, 10, 11, 13, 14, 15, 16, 18, 19, 21, 23],
'Número 2': [1, 2, 4, 5, 6, 7, 9, 10, 11, 14, 15, 18, 19, 22, 23],
'Número 3': [1, 2, 4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 18, 21, 22],
'Número 4': [1, 2, 4, 5, 7, 10, 11, 13, 15, 16, 18, 19, 21, 22, 23],
'Número 5': [1, 4, 5, 6, 7, 9, 10, 14, 15, 16, 18, 19, 21, 22, 23],
'Número 6': [1, 2, 4, 5, 6, 7, 9, 10, 11, 13, 14, 19, 21, 22, 23],
'Número 7': [1, 4, 5, 6, 7, 9, 10, 11, 13, 15, 16, 18, 19, 21, 22],}

#show_result(d, win)