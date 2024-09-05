from Verify import *
from Tests.section import createSecGame


def show_result(dic:dict, game_win):

    def noRepeatInList(l:list):
        auxList =[]
        for i in range(1,26):
            if i not in l:
                auxList.append(i)
        return auxList

    _res = quantidade_numeros_sorteados(dic, game_win)
    imprimir_lista_verde(sorted(game_win))
    print(noRepeatInList(game_win))
    print(createSecGame(game_win))
    imprimir_jogos_destacando(dic, game_win)
    render(_res)

