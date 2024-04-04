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

#import random
#
#def gerar_jogo_lotofacil():
#    jogo_lotofacil = random.sample(range(1, 26), 15)
#    return sorted(jogo_lotofacil)
#
#def gerar_varios_jogos_lotofacil(quantidade):
#    jogos_lotofacil = {}
#    for i in range(quantidade):
#        jogos_lotofacil[f'Jogo_{i+1}'] = gerar_jogo_lotofacil()
#    return jogos_lotofacil
#
#quantidade_jogos = 10
#jogos_lotofacil_gerados = gerar_varios_jogos_lotofacil(quantidade_jogos)

# Imprimindo os jogos gerados
#for chave, valor in jogos_lotofacil_gerados.items():
#    print(f"{chave}: {valor}")


