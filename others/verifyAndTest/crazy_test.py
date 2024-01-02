from random import *
from Game import *

def gerar_jogo(_dic):
    game = []
    i = 0
    while i < 15:
        number = random.randint(1, 25)
        if number not in game and number not in _dic:
            game.append(number) 
            i += 1
    game.sort()
    return game

def gerar_sequencia(qtd):
    dic = []
    for _ in range(qtd):
        num = random.randint(1,25)
        if num not in dic:
            dic.append(num)
    return dic

def principal(qtd_jogos, qtd_numeros):
    for _ in range(qtd_jogos):
        dic = gerar_sequencia(qtd_numeros)
        print(sorted(dic))
        print(gerar_jogo(dic))
        print('')


principal(10,6)