win = [1,3,4,5,8,10,11,14,15,16,20,21,23,24,25]
_not = [2,6,9,12,13,17,18,22]
dic = {'Jogo 1': {1, 3, 4, 5, 7, 8, 10, 11, 14, 15, 20, 21, 23, 24, 25},
'Jogo 2': {1, 3, 4, 5, 8, 10, 11, 14, 15, 16, 20, 21, 23, 24, 25},
'Jogo 3': {1, 3, 4, 5, 7, 8, 10, 11, 14, 15, 16, 20, 21, 24, 25},
'Jogo 4': {1, 3, 4, 5, 7, 8, 10, 11, 14, 15, 20, 21, 23, 24, 25},
'Jogo 5': {1, 3, 4, 5, 7, 8, 10, 11, 14, 15, 16, 20, 21, 23, 25},
'Jogo 6': {3, 4, 5, 7, 8, 10, 11, 14, 15, 16, 20, 21, 23, 24, 25},
'Jogo 7': {1, 3, 4, 5, 7, 8, 10, 11, 15, 16, 20, 21, 23, 24, 25},
'Jogo 8': {1, 3, 5, 7, 8, 10, 11, 14, 15, 16, 20, 21, 23, 24, 25},
'Jogo 9': {3, 4, 5, 7, 8, 10, 11, 14, 15, 16, 20, 21, 23, 24, 25},
'Jogo 10': {1, 3, 4, 5, 7, 8, 10, 14, 15, 16, 20, 21, 23, 24, 25},
'Jogo 11': {1, 3, 4, 5, 7, 10, 11, 14, 15, 16, 20, 21, 23, 24, 25},
'Jogo 14': {1, 3, 5, 7, 8, 10, 11, 14, 15, 16, 20, 21, 23, 24, 25},
'Jogo 15': {1, 3, 4, 5, 7, 8, 10, 11, 14, 15, 16, 21, 23, 24, 25},
'Jogo 16': {1, 4, 5, 7, 8, 10, 11, 14, 15, 16, 20, 21, 23, 24, 25},
'Jogo 17': {1, 3, 4, 5, 7, 8, 10, 11, 14, 15, 16, 20, 21, 23, 24},
'Jogo 18': {1, 3, 4, 5, 7, 8, 10, 11, 14, 16, 20, 21, 23, 24, 25},
'Jogo 19': {1, 3, 4, 5, 7, 8, 10, 11, 15, 16, 20, 21, 23, 24, 25},
'Jogo 20': {1, 4, 5, 7, 8, 10, 11, 14, 15, 16, 20, 21, 23, 24, 25},}

def quantidade_numeros_sorteados(dic, win):
    numeros_sorteados_vencedor = set(win)

    quantidades_por_jogo = {}

    for jogo, numeros_sorteados in dic.items():
        numeros_sorteados_conjunto = set(numeros_sorteados)
        quantidade_sorteados = len(numeros_sorteados_vencedor.intersection(numeros_sorteados_conjunto))
        quantidades_por_jogo[jogo] = quantidade_sorteados

    return quantidades_por_jogo

def imprimir_jogos_destacando(dic, win):
    def verde(texto):
        return f'\033[92m{texto}\033[0m'

    for jogo, numeros_sorteados in dic.items():
        numeros_formatados = [verde(str(num)) if num in win else str(num) for num in numeros_sorteados]

        print(f"{jogo}: {', '.join(numeros_formatados)}")

def imprimir_lista_verde(lista):
    def verde(texto):
        return f'\033[92m{texto}\033[0m'

    numeros_formatados = [verde(str(num)) for num in lista]

    amarela("\nJogo Sorteado: ")
    print(', '.join(numeros_formatados))
    print('\n')

def amarela(texto):
    def amarelo(texto):
        return f'\033[93m{texto}\033[0m'

    print(amarelo(texto))


def render(result):
    for jogo, quantidade_sorteados in result.items():
        print(f"{jogo}: {quantidade_sorteados} números.")

_res = quantidade_numeros_sorteados(dic, win)

