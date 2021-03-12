import sys
import math

print(sys.argv[0] + '\n Hi, ' + sys.argv[1] + ' ' + sys.argv[2] +
      '. How are you?')
'''sys.argv[0] выводит навние файла(test.py)
IndexError: list index out of range. выдает такую ошибку, потому что
список аргументов пуст '''
print()

#print(2/0)
''' ZeroDivisionError: division by zero.'''

print(str(2 ** 3 ** 4) + '\n' + str(2 + 3 * 4) + '\n' + str(1 / 2 + 3))
''' сначала делается умножение/деление, потом сложение/вычитание.
в степенях 2**3**4 = 2**(3**4)'''
print()

print('123**45 = ' + str(123**45) + ' 123.0**45.0 = ' + str(123.0**45.0))
'''в первом случае число записывается в обычном виде, во втором случае
в десятичной форме числа (n*10^k), где -10 < n < 10'''
print()

print(math.sqrt(10))
# print(math.sqrt(-1))
'''аргумент должен быть неотрицательным'''
print()

print('hello')