from contextlib import nullcontext
import random

GCollection = {}

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

def countRepeatedNumbersDic(dic: dict):
    repeteadNumbers = {}
    for game in dic.values():
        for number in game:
            if number in repeteadNumbers:
                repeteadNumbers[number] += 1
            else:
                repeteadNumbers[number] = 1
    return repeteadNumbers

def printDic(dic: dict):
    if 0 in dic:
        for key, value in dic.items():
            print(f"'Jogo {int(key)+1}': {value},")
    elif 1 in dic:
        for key, value in dic.items():
            print(f"'Jogo {int(key)}': {value},")

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

    for k in range(qtd_numbers):
        NInput = int(input(f'{k+1}ª Número: '))
        DicNotNumber.append(NInput)
    for i in range(1, qtdGame):
        GCollection[i] = game(DicNotNumber)

    del GCollection[0]

##############
def WinNumber(WinGame, jogo):
    return len(set(WinGame) & set(jogo))

def RelationWinNumbers(game_lotofacil, WinnerGame):
    resultados = {}
    for jogo, numeros in game_lotofacil.items():
        numeros_sorteados = WinNumber(WinnerGame, numeros)
        resultados[jogo] = numeros_sorteados
    return resultados

winn = [1,3,4,7,9,13,14,15,16,17,18,19,21,22,24]
dic = {
    0: [3, 4, 6, 8, 9, 10, 11, 16, 18, 19, 20, 22, 23, 24, 25],
    1: [1, 2, 4, 6, 10, 11, 14, 15, 16, 17, 19, 20, 22, 23, 25],
    2: [3, 4, 6, 7, 8, 9, 10, 12, 15, 17, 19, 21, 22, 24, 25],
    3: [3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 17, 18, 20, 21, 25],
    4: [2, 4, 6, 7, 9, 11, 12, 13, 14, 15, 16, 19, 21, 23, 25],
    5: [3, 4, 6, 9, 10, 14, 15, 16, 17, 19, 20, 21, 23, 24, 25],
    6: [2, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 20, 23, 24, 25],
    7: [3, 4, 5, 6, 7, 9, 10, 13, 16, 17, 18, 20, 22, 24, 25],
    8: [1, 2, 4, 5, 6, 7, 9, 10, 12, 13, 14, 17, 18, 21, 22],
    9: [1, 3, 4, 7, 9, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24],
    10: [1, 2, 4, 5, 6, 8, 11, 12, 13, 15, 16, 17, 19, 21, 24]
    
}
printDic(countRepeatedNumbersDic(dic))