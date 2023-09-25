from nenh import *
from macro import AutoBet

def main():
    number = int(input('Quantidade de jogos: '))
    question = input('Deseja descartar algum número?[s/n] ')

    if question == 'n':
        GameGenerator(number)
    elif question == 's':
        GameGenerator_not_number(number+1)

    printDic(GCollection)
    print(f'Números não sorteados: {NoRepeat(GCollection)}')
    question = input('\nDeseja exibir quatidade de repetições?[s/n] ')
    if question=='s':
        print('\nRepetições: ')
        printDic(countRepeatedNumbersDic(GCollection))
    else:
        pass

    if GCollection:
        bet = input('Deseja realizar as apostas?[s/n] ')
        if bet == 's':
            AutoBet(GCollection)
        else:
            pass

if __name__ == '__main__':
    main()
