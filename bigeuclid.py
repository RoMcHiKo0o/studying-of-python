import sys


def bigeuclid(a: int, b: int):
    # первая часть это просто нахождение нода
    if (a**2 + b**2) > 0:
        a, b = max(abs(a), abs(b)), min(abs(a), abs(b))
        a0 = a  # сохранил начальные значения
        b0 = b
        d = [a]  # тут я добавил массив, чтоб хранить начальные числа и
        # остатки до нуля. [a, b, R1, R2, ..., Rn] где Ri — остаток
        if a != b:
            while b > 0:
                d += [b]  # заполенение массива
                a, b = b, a % b
        nod = a
    else:
        nod = 0
        # x и y это коэффиценты Безу ()
    x = 1
    y = (d[-1] - d[-3]) / d[-2]
    """ пусть массив остатков [197, 31, 11, 9, 2, 1].
    Тогда 9x + 2y = 1. x = 1, а y вычисляется"""
    for i in range(len(d) - 2, 1, -1):
        x, y = y, x - y * (d[i-2] // d[i-1])
        """x заменяется на y, а y вычисляется по формуле. Все формулы
        я нашел на личсточке, нашел зависимость"""
    if y > 0:  # тут просто красивый вывод, можно было и без этого
        return f'{x} * {a0} + {y} * {b0} = {nod}'
    else:
        return f'{x} * {a0} - {-y} * {b0} = {nod}'


if __name__ == "__main__": # это всё было в предыдущих прогах
    try:
        if len(sys.argv) == 3:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
        else:
            a = int(input())
            b = int(input())
        print(bigeuclid(a, b))
    except ValueError:
        print("Incorrect input!!!")
