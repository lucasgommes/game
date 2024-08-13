from ..Game import *
from Verify import *
from Tests.section import createSecGame
game_win = [4, 5, 8, 9, 10, 13, 14, 16, 17, 20, 21, 22, 23, 24, 25]
def noRepeatInList(l:list):
    auxList =[]
    for i in range(1,26):
        if i not in l:
            auxList.append(i)
    return auxList

# 4 : [4, 3, 1, 4, 3] 64 : [4, 2, 2, 3, 4] 62 : [3, 4, 3, 2, 3]
dic = {'Jogo 1': [2, 4, 6, 7, 12, 13, 14, 16, 17, 18, 20, 22, 23, 24, 25],
'Jogo 2': [4, 5, 8, 9, 10, 13, 14, 16, 17, 20, 21, 22, 23, 24, 25],
'Jogo 3': [2, 3, 6, 8, 11, 12, 13, 14, 16, 17, 18, 21, 22, 23, 24],
'Jogo 4': [3, 4, 7, 8, 10, 11, 13, 14, 16, 17, 18, 20, 21, 23, 25],
'Jogo 5': [2, 3, 6, 8, 10, 11, 12, 13, 17, 18, 20, 22, 23, 24, 25],
'Jogo 6': [2, 4, 5, 7, 8, 10, 12, 13, 14, 16, 18, 20, 21, 22, 23],
'Jogo 7': [2, 3, 4, 5, 8, 11, 12, 13, 16, 17, 18, 20, 21, 22, 24],}

_res = quantidade_numeros_sorteados(dic, game_win)
imprimir_lista_verde(sorted(game_win))
print(noRepeatInList(game_win))
print(createSecGame(game_win))
imprimir_jogos_destacando(dic, game_win)
render(_res)