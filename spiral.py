def prmatr(a):
	for i in range(len(a)):
		for j in range(len(a[0])):
			print(" "*(3-len(str(a[i][j]))), a[i][j], end="") # равное расстояние между числами для красоты
		print()
def prmatr2(a): #на степике prmatr не работает, это замена, по факту так даже лучше
	for i in a:
		for j in i:
			print(" " * (3 - len(str(j))), j, end="") # равное расстояние между числами для красоты
		print()
def transpmatr(a):
	c = [[0 for i in range(len(a))] for j in range(len(a[0]))]
	for i in range(len(a)):
		for j in range(len(a[0])):
			c[i][j] = a[j][i]
	return(c)
def revmatr(a):
	c = [[0 for i in range(len(a))] for j in range(len(a[0]))]
	for i in range(len(a)):
		for j in range(len(a[0])):
			c[i][j] = a[-i-1][j]
	return(c)
def spiralmatr(n):
	if n == 1:
		print(n)
	else:
		c = [[0 for i in range(n)] for j in range(n)]
		last = 1
		di = 0
		i = 0
		while (i-di) <= n:
			j = 0
			while j < n:
				if c[i-di][j] == 0:
					c[i-di][j] = last
					last += 1
				j += 1
			if c[i-di][n-(i-di)-1] != 0 and c[(i-di)+1][n-(i-di)-1] != 0:
				c = revmatr(transpmatr((c)))
			else:
				c = revmatr(transpmatr((c)))
				di += 1
			i += 1
			if last == n**2 + 1:
				break
		if n % 2 == 1:
			c = transpmatr(revmatr(c))
		else:
			c = revmatr(transpmatr(c))
		return(c)
n = int(input())
prmatr(spiralmatr(n))