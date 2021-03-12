import sys


n, r = int(sys.argv[1]), int(sys.argv[2])
i = 0
while r**(i + 1) <= n:
    i = i + 1
s = ''
while i >= 0:
    print(n, i, n // r**i)
    s = s + str(n // r**i)
    n -= (n // r**i) * (r ** i)
    i = i - 1
print(s)
