from Game import *
from Result import show_result


game_win = [2,4,7,9,11,12,13,15,18,19,20,21,23,24,25]


def main():
    number = int(input('Quantidade de jogos: '))
    quest = input('Deseja descartar algum número?[s/n] ')

    if quest == 'n':
        GameGenerator(number)
    elif quest == 's':
        GameGenerator_not_number(number+1)

    printDic(GCollection)
    print(f'Números não sorteados: {NoRepeat(GCollection)}')
    
    question = input('\nDeseja exibir quatidade de repetições?[s/n/c/sc]: ')

    if question=='s':
        print('\nRepetições: ')
        printDic(countRepeatedNumbersDic(GCollection))
    if question=='c':
        print("\nComparando resultados com game_win")
        show_result(GCollection, game_win)
    if question=='sc':
        print('\nRepetições: ')
        printDic(countRepeatedNumbersDic(GCollection))
        print("\nComparando resultados com game_win")
        show_result(GCollection, game_win)


if __name__ == '__main__':
    main()
