import random
import numpy as np
from Verify import (imprimir_jogos_destacando, imprimir_lista_verde,
                    quantidade_numeros_sorteados, render)


def initialize_vetor_60():
    return [2, 3, 6, 12, 13, 14,
            20, 24, 26, 34, 35, 37,
            40, 45, 46]

def remove_numbers(vetor_60, no_number):
    for num in no_number:
        if num in vetor_60:
            vetor_60.remove(num)
    return vetor_60

def select_random_numbers(vetor_60, num_to_remove):
    no_number = []
    for _ in range(num_to_remove):
        num = random.choice(vetor_60)
        vetor_60.remove(num)
        no_number.append(num)
    return no_number

def generate_vetores_de_6(vetor_60):
    vetores_de_6 = []
    while len(vetor_60) >= 6:
        try:
            numeros_escolhidos = np.random.choice(vetor_60, size=6, replace=False)
            vetores_de_6.append(numeros_escolhidos)
            vetor_60 = np.setdiff1d(vetor_60, numeros_escolhidos)
        except ValueError as e:
            print(f"Erro ao selecionar números: {e}")
            break
    return vetores_de_6

def main():
    vetor_60 = initialize_vetor_60()
    no_number = []  # Adicione números que deseja remover, se houver
    vetor_60 = remove_numbers(vetor_60, no_number)
    vetores_de_6 = generate_vetores_de_6(vetor_60)
    
    for i, vetor in enumerate(vetores_de_6):
        vetor_convertido = [int(num) for num in vetor]
        print(f"'{i + 1}': {sorted(vetor_convertido)},")
    
def verify():
    d = {}
    game_win = [6, 15, 18, 31, 32, 47]
    _res = quantidade_numeros_sorteados(d, game_win)
    imprimir_lista_verde(sorted(game_win))
    imprimir_jogos_destacando(d, game_win)
    render(_res)

def run():
    while True:
        answ = input('1: Main\n2: Verify\n--')
        if answ == '1':
            main()
            break
        elif answ == '2':
            verify()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    run()
