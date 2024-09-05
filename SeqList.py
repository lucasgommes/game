"""

    Cria sequências ponderando os números informados dentro de lista_numeros. É possível ajustar o tamanho da
    lista que será gerada, na variável 'selecionados', bem como, quantas listas serão geradas em 'num_combinacoes'.

"""


import random
from collections import defaultdict
from Result import show_result


game_win = [11, 18, 32, 39, 46, 48]


def gerar_combinacoes_ponderadas(lista_numeros, num_combinacoes):
    combinacoes = []
    contagem_numeros = defaultdict(int)
    
    # Pondera os pesos inicialmente com base na frequência dos números na lista
    pesos = [1] * len(lista_numeros)
    
    # Gera as combinações
    for _ in range(num_combinacoes):
        # Embaralha a lista para cada nova combinação
        random.shuffle(lista_numeros)
        
        # Seleciona os primeiros 6 números após o embaralhamento
        selecionados = lista_numeros[:6]
        
        # Adiciona a combinação na lista de combinações
        combinacoes.append(selecionados)
        
        # Atualiza a contagem de números selecionados
        for num in selecionados:
            contagem_numeros[num] += 1
    
    return combinacoes, contagem_numeros


# Exemplo de uso: 8, 11, 19, 39, 47, 48
lista_numeros = [8,11,18,19,
                 46,32,39,
                 48,47]
num_combinacoes = 10


combinacoes, contagem_numeros = gerar_combinacoes_ponderadas(lista_numeros, num_combinacoes)


# Imprime as combinações geradas
for i, combinacao in enumerate(combinacoes, 1):
    print(f"'Jogo {i}': {sorted(combinacao)},")


# Imprime a quantidade de vezes que cada número foi selecionado
print("\nContagem de seleções por número:")
for numero, quantidade in contagem_numeros.items():
    print(f"Número {numero}: {quantidade} vezes")


quest = input('Comparar resultados? [s/n]')
if quest=='s':
    dic = {i: value for i, value in enumerate(combinacoes)}
    show_result(dic, game_win)
