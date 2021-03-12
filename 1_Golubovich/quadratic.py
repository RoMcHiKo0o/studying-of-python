import math
import sys

b = float(sys.argv[1])

c = float(sys.argv[2])

d = b * b - 4 * c
print('x^2+' + sys.argv[1] + 'x+' + sys.argv[2])
if d > 0:
    print('два корня')
    d = math.sqrt(d)
elif d == 0:
    print('один корень')
else:
    print('нет корней, дискриминант меньше нуля')

print('x1 = ' + str((-b+d) / 2))

print('x2 = ' + str((-b-d) / 2))
