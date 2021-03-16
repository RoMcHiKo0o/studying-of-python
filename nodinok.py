import sys


def gcd(a: int, b: int) -> int:
    if (a**2 + b**2) > 0:
        a, b = max(abs(a), abs(b)), min(abs(a), abs(b))
        # тут я сделал a > b и сделал их положительными,
        # потому что прога не проходила тест на отрицательные числа
        # нод(a, b) = нод(-a, b)
        if a != b:
            while b > 0:
                a, b = b, a % b
                # a становится b, b становится остатком
        else:
            nod = a
        nod = a
        return nod
    else:
        return 0


def lcm(a: int, b: int) -> int:
    if a * b == 0:
        return 0
    else:
        return abs(a * b) // gcd(a, b)


if __name__ == '__main__':
    try:
        if len(sys.argv) == 3:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
        else:
            a = int(input())
            b = int(input())
        print(a, b, '->', gcd(a, b), lcm(a, b))
    except ValueError:
        print("Incorrect input!!!")
