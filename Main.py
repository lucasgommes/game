from nenh import GameGenerator, printDic, countRepeatedNumbersDic, GCollection, NoRepeat
def main():
    number = int(input('Quantidade de jogos: '))
    GameGenerator(number)
    print(f'Números não presentes: {NoRepeat(GCollection)}')
    question = input('\nDeseja exibir quatidade de repetições? (y/n)')
    if question=='y':
        print('\nRepetições: ')
        printDic(countRepeatedNumbersDic(GCollection))
    else:
        pass

if __name__ == '__main__':
    main()