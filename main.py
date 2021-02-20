import nodinok # импорт модуля
a, b = int(input()), int(input())
c, d = 4.1, 5 # создано специально чтоб словить ошибку
print(nodinok.gcd(a, b), nodinok.lcm(a, b))
print(nodinok.gcd(c, d), nodinok.lcm(c, d))
