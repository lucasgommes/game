import math
from random import shuffle
import random


# comb = math.comb(16, 15)
# print(comb)

# li = list(range(1,26))
# random.shuffle(li)
# print(sorted(li[:20]))



# vet = []
# while len(vet)<30:
#     number = random.randint(1, 60)
#     if number not in vet:
#         vet.append(number)
# print(sorted(vet))

def create_ses(qtd_ses: int, length: int):
    vet = []
    count = 0

    while len(vet) < length:

        init_interval = 1 + count
        final_interval = 11 + count

        vet.extend(random.sample(range(init_interval, final_interval), qtd_ses))

        count += 10

        if len(vet) > length:
            vet = vet[:length]

    return sorted(vet)

print(create_ses(3, 20))
