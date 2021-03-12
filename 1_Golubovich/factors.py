import sys


n = int(sys.argv[1])
factor = 2
factor0 = factor
n0 = n
while factor ** 2 <= n0:
    if n % factor == 0:
        print(factor)
        n /= factor
    else:
        factor += 1
