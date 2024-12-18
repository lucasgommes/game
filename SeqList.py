"""

    Cria sequências com os números informados dentro de lista_numeros. É possível ajustar o tamanho da
    lista que será gerada, na variável 'selecionados', bem como, quantas listas serão geradas em 'num_combinacoes'.

"""


import random
from collections import defaultdict
from Result import show_result
from Game import countRepeatedNumbersDic, printDic


game_win = [10,24,29,38,41,46]
formation = [2,4]

def gerar_combinacoes(lista_numeros, num_combinacoes):
    combinacoes = []
    contagem_numeros = defaultdict(int)

    
    # Gera as combinações
    while len(combinacoes) < num_combinacoes:
        # Embaralha a lista para cada nova combinação
        random.shuffle(lista_numeros)
        
        # Seleciona os primeiros 6 números após o embaralhamento
        selecionados = sorted(lista_numeros[:6])
        
        # Adiciona a combinação na lista de combinações
        maiores_30 = [n for n in selecionados if n >= 30]
        menores_30 = [n for n in selecionados if n <= 30]
        if formation[0] == len(menores_30) and formation[1] == len(maiores_30):
            combinacoes.append(selecionados)
            
        # Atualiza a contagem de números selecionados
            for num in selecionados:
                contagem_numeros[num] += 1
    
    return combinacoes, contagem_numeros

lista_numeros = [1,6,10,33,35,38,
                 12,17,18,22,24,29,
                 41,46,49]
num_combinacoes = 7


combinacoes, contagem_numeros = gerar_combinacoes(lista_numeros, num_combinacoes)


# Imprime as combinações geradas
for i, combinacao in enumerate(combinacoes, 1):
    print(f"'Seq {i}': {sorted(combinacao)},")


# Imprime a quantidade de vezes que cada número foi selecionado
print("\nContagem de seleções por número:")
cont = dict(sorted(contagem_numeros.items()))
for numero, quantidade in cont.items():
    print(f"Número {numero}: {quantidade} vezes")



quest = input('Comparar resultados? [s/n]')
if quest=='s':
    dic = {i: value for i, value in enumerate(combinacoes)}
    show_result(dic, game_win)
    