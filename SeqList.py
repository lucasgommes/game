"""

    Cria sequências com os números informados dentro de lista_numeros. É possível ajustar o tamanho da
    lista que será gerada, na variável 'selecionados', bem como, quantas listas serão geradas em 'num_combinacoes'.

"""


import random
from collections import defaultdict
from Result import show_result


game_win = [10,16,35,46,49,60]


def gerar_combinacoes(lista_numeros, num_combinacoes):
    combinacoes = []
    contagem_numeros = defaultdict(int)

    
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



lista_numeros = [2, 5, 7, 13, 14, 15, 21, 23, 24, 35, 36, 38, 41, 44, 50, 51, 54, 55]
num_combinacoes = 6


combinacoes, contagem_numeros = gerar_combinacoes(lista_numeros, num_combinacoes)


# Imprime as combinações geradas
for i, combinacao in enumerate(combinacoes, 1):
    print(f"'Seq {i}': {sorted(combinacao)},")


# Imprime a quantidade de vezes que cada número foi selecionado
print("\nContagem de seleções por número:")
for numero, quantidade in contagem_numeros.items():
    print(f"Número {numero}: {quantidade} vezes")


quest = input('Comparar resultados? [s/n]')
if quest=='s':
    dic = {i: value for i, value in enumerate(combinacoes)}
    show_result(dic, game_win)
