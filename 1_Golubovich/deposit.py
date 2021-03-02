import sys


def depositformonth(s, y, p):
    for i in range(12 * y):
        s += s * p / 12
    return s


def depositforday(s, y, p):
    for i in range(365 * y):
        s += s * p / 365
    return s



def depositforsecond(s, y, p):
    for i in range(365 * 3600 * y):
        s += s * p / 365 / 3600
    return s


n, year, proc = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
print(depositformonth(n, year, proc))
print(depositforday(n, year, proc))
print(depositforsecond(n, year, proc))
