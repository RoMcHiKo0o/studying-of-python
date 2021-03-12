import sys


def fib(n: int):
    if type(n) == int and n >= 0:  # проверка типа и чтоб было
        # неотрицательным
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    else:
        return "wrong input"


def fibfast(n: int):
    if type(n) == int and n >= 0:  # проверка типа и чтоб было
        # неотрицательным
        dict = {0: 0, 1: 1}  # словарь значений, чтоб не пересчитать
        # каждое значение по куче раз
        i = 0
        for i in range(n + 1):
            if i not in dict.keys():
                dict[i] = dict[i - 1] + dict[i - 2]
        return dict[n]
    else:
        return "wrong input"


if __name__ == '__main__':
    # n = int(sys.argv[1])  при 25 и меньше еще норм
    # print(str(n) + "th element is", fib(n))
    n = int(sys.argv[1])
    print(str(n) + "th element is", fibfast(n))
