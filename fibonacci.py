import sys


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibfast(n: int) ->int:
    dict = {0: 0, 1: 1}  # словарь значений, чтоб не пересчитать
    # каждое значение по куче раз
    i = 0
    for i in range(n + 1):
        if i not in dict.keys():
            dict[i] = dict[i - 1] + dict[i - 2]
    return dict[n]


if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            a = int(sys.argv[1])
        else:
            a = int(input())
        print(f'{a}-ое число Фибоначчи равно {fibfast(a)}')
    except ValueError:
        print("Incorrect input!!!")
