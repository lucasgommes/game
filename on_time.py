from Result import noRepeatInList, show_result

dic = {'Número 1': [1, 4, 6, 7, 8, 9, 10, 12, 13, 15, 18, 21, 22, 23, 24],
'Número 2': [5, 6, 7, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 25],
'Número 3': [3, 4, 7, 8, 9, 10, 12, 13, 15, 18, 21, 22, 23, 24, 25],
'Número 4': [4, 6, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 23, 24],
'Número 5': [3, 4, 6, 7, 8, 9, 10, 11, 12, 16, 18, 20, 23, 24, 25],
'Número 6': [1, 3, 5, 7, 8, 10, 11, 13, 15, 19, 20, 21, 22, 23, 24],
'Número 7': [1, 3, 4, 5, 7, 9, 10, 11, 13, 16, 18, 19, 20, 22, 25]}


lis = []

while len(lis) < 15:
    inp = int(input(f'{sorted(lis)} <-- '))
    lis.append(inp)
    show_result(dic, lis)
print(sorted(lis))
print(noRepeatInList(lis))

