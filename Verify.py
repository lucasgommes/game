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
