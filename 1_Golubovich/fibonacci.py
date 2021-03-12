import sys


def fib(r):  # до 30, а потом медленооо
    if r == 1 or r == 2:
        return 1
    else:
        return fib(r - 1) + fib(r - 2)


n = int(sys.argv[1])
print(fib(1))
for i in range(2, n+1):
    print(str(i) + 'ое ', 'число =', fib(i),
          'отношение =', fib(i + 1)/fib(i))
