from Game import *
from Verify import *
from section import createSecGame
game_win = [22,12,7,21,1,20,6,15,5,25,18,13,4,23,3]
def noRepeatInList(l:list):
    auxList =[]
    for i in range(1,26):
        if i not in l:
            auxList.append(i)
    return auxList

# 4 : [4, 3, 1, 4, 3] 64 : [4, 2, 2, 3, 4] 62 : [3, 4, 3, 2, 3]

dic = {'Jogo 1': [1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 19, 23],
'Jogo 2': [1, 3, 4, 6, 7, 10, 11, 12, 13, 18, 19, 20, 23, 24, 25],
'Jogo 3': [1, 3, 4, 5, 7, 11, 12, 14, 15, 16, 18, 19, 23, 24, 25],
'Jogo 4': [1, 4, 5, 7, 8, 12, 13, 14, 16, 17, 18, 19, 20, 24, 25],
'Jogo 5': [3, 4, 5, 6, 8, 11, 12, 14, 15, 16, 17, 18, 19, 23, 24],}

_res = quantidade_numeros_sorteados(dic, game_win)
imprimir_lista_verde(sorted(game_win))
print(noRepeatInList(game_win))
print(createSecGame(game_win))
imprimir_jogos_destacando(dic, game_win)
render(_res)