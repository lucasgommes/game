from itertools import product

def find_combinations():
    numbers = [1, 2, 3, 4, 5]
    combinations = []

    for combination in product(numbers, repeat=5):
        if sum(combination) == 15:
            combinations.append(combination)

    return combinations

result = find_combinations()
cont=0
for combination in result:
    cont+=1
    print(cont,'-',combination)