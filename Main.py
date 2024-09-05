from Game import *
from Result import show_result


game_win = [3, 4, 5, 6, 8, 9, 10, 11, 12, 15, 17, 18, 21, 24, 25]


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
