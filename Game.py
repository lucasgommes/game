from contextlib import nullcontext
import random

GCollection = {}


def countRepeatedNumbersDic(dic: dict):
    repeteadNumbers = {}
    for game in dic.values():
        for number in game:
            if number in repeteadNumbers:
                repeteadNumbers[number] += 1
            else:
                repeteadNumbers[number] = 1
    return repeteadNumbers


def generateGame():
    game = []
    i = 0
    while i < 15:
        number = random.randint(1, 25)
        if number not in game:
            game.append(number) 
            i += 1
    game.sort()
    return game


def game(not_number:dict=None):
    game_result = []

    while len(game_result) < 15:
        collection = countRepeatedNumbersDic(GCollection)
        max_repeat = max(collection.values())
        min_repeat = min(collection.values())
        number = random.randint(1, 25)

        if not_number:
            if (number not in game_result and number not in not_number) and ((collection.get(number, 0) <= max_repeat+2) and (collection.get(number, 0) >= min_repeat)):
                game_result.append(number)
        else:
            if number not in game_result and (collection.get(number, 0) <= max_repeat+2) and (collection.get(number, 0) >= min_repeat):
                game_result.append(number)
    return sorted(game_result)


def CountRepeated(number : int, dic : dict):
    repeat = 0
    RepeatedList = countRepeatedNumbersDic(dic)
    
    for _ in RepeatedList.items():
        if number in RepeatedList:
            repeat = RepeatedList[number]
        else:
            repeat = 0
    return repeat


def printDic(dic: dict):
    if 0 in dic:
        for key, value in dic.items():
            print(f"'Jogo {int(key)+1}': {value},")
    else:
        for key, value in dic.items():
            print(f"'Número {int(key)}': {value},")


def NoRepeat(dic:dict):
    numbers = []
    auxDic = countRepeatedNumbersDic(dic)

    for i in range(1,26):
        if i in auxDic:
            pass
        else:
            numbers.append(i)
    return sorted(numbers)      


def GameGenerator(qtdGame:int):
    GCollection[0] = generateGame()
    GCollection[1] = generateGame()

    for i in range(len(GCollection), qtdGame):
        GCollection[i] = game()


def GameGenerator_not_number(qtdGame:int):
    GCollection[0] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    GCollection[1] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

    qtd_numbers = int(input('Informe a quantidade de números que não serão adiconados: '))
    DicNotNumber = []
    
    if qtd_numbers == 99:
        n2input = int(input('Quatidade: '))
        for _ in range(n2input):
                nremove = random.randint(1,25)
                DicNotNumber.append(nremove)

    elif qtd_numbers != 99:
        for k in range(qtd_numbers):
            NInput = int(input(f'{k+1}ª Número: '))
            DicNotNumber.append(NInput)

    for i in range(1, qtdGame):
        GCollection[i] = game(DicNotNumber)

    del GCollection[0]


def verify_repeat(jogos):
    jogos_repetidos = []
    for jogo1, numeros1 in jogos.items():
        for jogo2, numeros2 in jogos.items():
            if jogo1 != jogo2 and set(numeros1) == set(numeros2):
                jogos_repetidos.append((jogo1, jogo2))

    if jogos_repetidos:
        print("Jogos repetidos:")
        for repeticao in jogos_repetidos:
            print(f"{repeticao[0]} e {repeticao[1]} têm números idênticos.")
    else:
        print("Não há jogos repetidos.")