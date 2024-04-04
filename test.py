from Game import *
from Verify import *
from section import createSecGame
game_win = [14,23,13,3,24,19,21,25,20,8,11,15,10,7,5]
def noRepeatInList(l:list):
    auxList =[]
    for i in range(1,26):
        if i not in l:
            auxList.append(i)
    return auxList

# 4 : [4, 3, 1, 4, 3] 64 : [4, 2, 2, 3, 4] 62 : [3, 4, 3, 2, 3]
print(generateGame())
dic = {'Jogo 5': [1, 4, 6, 7, 8, 9, 11, 12, 14, 17, 18, 20, 21, 22, 23],

'Jogo 6': [1, 3, 6, 9, 10, 11, 12, 13, 14, 15, 17, 20, 21, 22, 23],

'Jogo 7': [1, 3, 5, 6, 8, 9, 12, 13, 14, 16, 17, 18, 22, 23, 24],

'Jogo 8': [1, 3, 4, 5, 6, 7, 8, 9, 12, 13, 15, 16, 18, 20, 22],

'Jogo 9': [3, 4, 5, 6, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23],

'Jogo 10': [3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 16, 20, 22, 23, 24]}

_res = quantidade_numeros_sorteados(dic, game_win)
imprimir_lista_verde(sorted(game_win))
print(noRepeatInList(game_win))
print(createSecGame(game_win))
imprimir_jogos_destacando(dic, game_win)
render(_res)