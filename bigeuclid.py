import sys


def bigeuclid(a: int, b: int):
    a, b = max(a, b), min(a, b)
    if a * b == 0:  # здесь сразу отсеиваю случаи, когда нули, равные и
        # противоположные числа
        return f'0 * {a} + 0 * {b} = 0'
    elif (a - b) * (a + b) == 0:
        return f' {a} + ({- a // b}) * {b} = 0'
    else:  # нахождение нода
        a0 = a  # сохранил начальные значения
        b0 = b
        d = [a]  # тут я добавил массив, чтоб хранить начальные числа и
        # остатки. [a, b, R1, R2, ..., Rn] где Ri — остаток
        while b != 0:
            d += [b]  # заполенение массива
            a, b = b, a % b
        nod = a
    # x и y это коэффиценты Безу ()
    if nod == b0 or nod == -b0:
        """случаи когда остаток будет ноль
        я выбрал такое решение, в котором этот случай выдает ошибку,
        поэтому приходится делать проверку"""
        return f'{a0} + ({int(-a0 / b0)}) * {b0} = 0'
    if nod == a0 or nod == -a0:
        return f'{b0} + ({int(-b0 / a0)}) * {a0} = 0'
    x = 1
    y = (d[-1] - d[-3]) / d[-2]
    """ пусть массив остатков [197, 31, 11, 9, 2, 1].
    Тогда 9x + 2y = 1. x = 1, а y выражается"""
    for i in range(len(d) - 2, 1, -1):
        x, y = y, x - y * (d[i - 2] // d[i - 1])
        """x заменяется на y, а y вычисляется по формуле. Все формулы
        я вывел на листочке, нашел зависимость"""
    if y > 0:  # тут просто красивый вывод, можно было и без этого
        return f'{int(x)} * {a0} + {int(y)} * {b0} = {nod}'
    else:
        return f'{int(x)} * {a0} - {int(-y)} * {b0} = {nod}'


if __name__ == "__main__":  # это всё было в предыдущих прогах
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