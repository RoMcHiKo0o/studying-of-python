import sys


n = int(sys.argv[1])
i = 1
while n > 0:
    n -= 1 / i
    i += 1
print(i)
