import random
from generateGame import countRepeatedNumbersDic

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

def game():
    game_result = []
    while len(game_result) < 15:
        collection = countRepeatedNumbersDic(GCollection)
        max_repeat = max(collection.values())
        min_repeat = min(collection.values())
        number = random.randint(1, 25)

        if number not in game_result and (collection.get(number, 0) <= max_repeat+2) and (collection.get(number, 0) >= min_repeat):#and (collection.get(number, 0) >= min_repeat)
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
    sorted(dic)
    for key, value in dic.items():
        print(f"número {int(key)}: {value}")

def GameGenerator(qtdGame:int):
    GCollection[0] = generateGame()
    GCollection[1] = generateGame()
    #GCollection[0] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    for i in range(len(GCollection), qtdGame):
        GCollection[i] = game()
    printDic(GCollection)