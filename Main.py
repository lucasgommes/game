from nenh import GameGenerator, printDic, countRepeatedNumbersDic, GCollection
def main():
    number = int(input('Quantidade de jogos: '))
    GameGenerator(number)
    question = input('\nDeseja exibir qtd de repetições? (y/n)')
    if question=='y':
        print('\nRepetições: ')
        printDic(countRepeatedNumbersDic(GCollection))
    else:
        pass

if __name__ == '__main__':
    main()