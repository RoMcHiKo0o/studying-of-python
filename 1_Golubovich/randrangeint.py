import random
import sys

a, b = int(sys.argv[1]), int(sys.argv[2])
print(random.uniform(a, b + 1))
'''снизу я решил посчитать за сколько попыток выпадет каждое число, просто так'''
for i in range(a, b+1):
    c = 1
    while int(random.uniform(a, b + 1)) != i:
        c += 1
    print(i, ' выпал за ', c)
