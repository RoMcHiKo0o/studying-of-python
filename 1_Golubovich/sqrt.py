import math
import sys


def mysqrt1(a, e):
    b = a
    while abs(a - b/a) > e:
        a = (a + b/a) / 2.0
    return a


c = int(sys.argv[1])
print('моя функция: ', mysqrt1(c, 1e-10))
print('math.sqrt:   ', math.sqrt(c))
