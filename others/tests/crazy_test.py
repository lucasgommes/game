from collections import Counter

conjuntos = {1: [5, 4, 1, 1, 4], 
2: [5, 4, 2, 2, 2],
3: [3, 3, 5, 1, 3],
4: [4, 2, 4, 3, 2],
5: [1, 4, 3, 4, 3],
6: [4, 4, 2, 3, 2],
7: [1, 4, 4, 2, 4],
8: [2, 3, 4, 4, 2],
9: [3, 3, 3, 4, 2],
10: [4, 4, 1, 4, 2],
11: [3, 1, 4, 2, 5],
12: [3, 4, 2, 5, 1],
13: [1, 1, 5, 4, 4],
14: [3, 2, 3, 4, 3],
15: [4, 1, 4, 2, 4],
16: [3, 3, 5, 4, 0],
17: [3, 0, 4, 4, 4],
18: [5, 2, 4, 1, 3],
19: [3, 3, 2, 3, 4],
20: [5, 2, 3, 3, 2],
}

def encontrar_conjuntos_semelhantes(conjuntos):
    conjuntos_semelhantes = {}
    contagem = Counter(tuple(sorted(c)) for c in conjuntos.values())
    for conjunto, count in contagem.items():
        if count > 1:
            conjuntos_semelhantes[conjunto] = [chave for chave, valor in conjuntos.items() if tuple(sorted(valor)) == conjunto]
    return conjuntos_semelhantes

conjuntos_semelhantes = encontrar_conjuntos_semelhantes(conjuntos)
print("Conjuntos semelhantes:")
for conjunto, conjuntos_id in conjuntos_semelhantes.items():
    print("Conjunto:", conjunto, "Conjuntos:", conjuntos_id)
