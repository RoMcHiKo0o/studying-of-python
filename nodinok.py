def nod(a, b):
	if type(a) == int and  type(b) == int: #проверка на тип int
		if a < b:
			a, b = b, a # сделал чтоб a > b
		if a != b: 
			while b > 0:
				a, b = b, a % b
				#алгоритм евклида. a становится b, b становится остатком
		else:
			nod = a
		nod = a
		return nod
	else:
		return "input error, type of numbers should be int"
def nok(a, b):
	if type(a) == int and  type(b) == int:# такая же проверка как и в НОД
		return int(a * b / nod(a, b))
	else:
		return ""
a, b = int(input()), int(input())
c, d = 4.1, 5 # создано специально чтоб словить ошибку
print (nod(a, b), nok(a, b))
print (nod(c, d), nok(c, d))