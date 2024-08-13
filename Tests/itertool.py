"""

    Exibe todas as possibilidades de combinações entres os valores
    inserido na lista 'números'.

"""

import itertools

def fechamento(numeros, tamanho_sequencia):
    todas_combinacoes = list(itertools.combinations(numeros, tamanho_sequencia))
    todas_combinacoes = [list(comb) for comb in todas_combinacoes]
    return todas_combinacoes

# Exemplo de uso
numeros = [6, 18, 15,
            31, 32, 34, 40, 42, 45,
            47, 2, 19, 51, 56, 60]


tamanho_sequencia = 6
todas_sequencias = fechamento(numeros, tamanho_sequencia)
cont = 0

for sequencia in todas_sequencias:
    cont+=1
    print(f"{cont}:{sequencia}")



