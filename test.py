from Game import *
from Verify import *
from section import createSecGame
game_win = [17, 19, 14, 10, 8, 18, 2, 24, 4, 23, 15, 1, 7, 11, 6]
def noRepeatInList(l:list):
    auxList =[]
    for i in range(1,26):
        if i not in l:
            auxList.append(i)
    return auxList

# 4 : [4, 3, 1, 4, 3] 64 : [4, 2, 2, 3, 4] 62 : [3, 4, 3, 2, 3]

dic = {'Jogo 1': [1, 2, 3, 4, 7, 8, 9, 10, 13, 14, 16, 18, 19, 21, 23],
'Jogo 2': [1, 2, 6, 7, 8, 10, 11, 12, 13, 17, 19, 21, 23, 24, 25],
'Jogo 3': [1, 2, 3, 5, 7, 10, 11, 13, 17, 18, 19, 21, 23, 24, 25],
'Jogo 4': [1, 2, 3, 4, 6, 7, 8, 10, 11, 13, 15, 16, 20, 24, 25],
'Jogo 5': [1, 4, 6, 8, 10, 11, 12, 13, 14, 18, 19, 21, 22, 23, 24],
'Jogo 6': [1, 3, 4, 6, 9, 11, 14, 16, 17, 18, 19, 21, 22, 24, 25],
'Jogo 7': [3, 4, 5, 6, 7, 11, 12, 14, 16, 17, 18, 20, 23, 24, 25],
'Jogo 8': [2, 3, 4, 6, 9, 10, 11, 12, 14, 15, 17, 18, 21, 23, 24],
'Jogo 9': [2, 3, 5, 6, 10, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23],
'Jogo 10': [2, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 21, 23, 25],}

_res = quantidade_numeros_sorteados(dic, game_win)
imprimir_lista_verde(sorted(game_win))
print(noRepeatInList(game_win))
print(createSecGame(game_win))
imprimir_jogos_destacando(dic, game_win)
render(_res)