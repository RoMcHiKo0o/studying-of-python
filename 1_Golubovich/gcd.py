import sys


def gcd(a, b):
    if type(a) == int and type(b) == int:  # проверка на тип int
        if a < b:
            a, b = b, a  # сделал чтоб a > b
        if a != b:
            while b > 0:
                a, b = b, a % b
            # алгоритм евклида. a становится b, b становится остатком
        else:
            nod = a
        nod = a
        print(nod)
    else:
        print("input error, type of numbers should be int")


a, b = int(sys.argv[1]), int(sys.argv[2])
gcd(a, b)
