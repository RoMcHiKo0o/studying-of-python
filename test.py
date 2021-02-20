def my_func1(str):
 	print(', '.join(str))
def iq_test(numbers):
	e1 = [int(i) for i in range(len(numbers.split())) if int(numbers.split()[i]) % 2 == 1]
	e0 = [int(i) for i in range(len(numbers.split())) if int(numbers.split()[i]) % 2 == 0]
	if len(e1)>len(e0):
		print(e0[0]+1)
	else:
		print(e1[0]+1)
	#iq_test("1 3 3 1 4 33")
def song_decoder(song):
    print(" ".join(song.replace('WUB', ' ').split()))
    print(song.replace('WUB', ' ').split())
    #song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
def my_input():
	a= int(input())
	b=int(input())
	print(a+b) #my_input()
i = 0
def star():
	while i < 5:
		print(i, '*')
		if i % 2 == 0:
			print(i, '**')
		if i > 2:
			print(i, '***')
		i = i + 1 #star()
def nod(a,b):
	if a < b:
		a, b = b, a
	if a != b:
		while b > 0:
			a, b = b, a % b
	else:
		return a
	return a #print (nod(5,7))
def shet(s):
	s2 = ""
	c = 1
	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			c += 1
			if i == len(s) - 2:
				s2 = s2 + s[-2] + str(c)
		else:
			s2 = s2 + s[i - c + 1] + str(c)
			c = 1
		if i == len(s) - 2 and c == 1:
			s2 = s2 + s[-3] + str(1)
	if len(s) == 1:
		return s+str(1)
	else:
		return s2
def cons_matr(n):
	a = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			a[i][j] = n * i + (j + 1)
	return(a)
def prmatr(a):
	for i in range(len(a)):
		for j in range(len(a[0])):
			print(" "*(3-len(str(a[i][j]))), a[i][j], end="")
		print()
n = int(input())
# n 2*(n-1) n-2 n-2 2*(n-3) n-4 n-4 2*(n-5) n-6
# f[s] = 4n-(2*(1+2*s)+2*s+2s+2) = 4n - 8*s -4 = 4*(n-2*s-1) - 1 первый шаг начинается с нуля
# n 3*(n-1) n-2 3*(n-3) n-4 3*(n-5)
# f[s] = 4n-3*(1+2*s)
c = [[0 for i in range(n)] for j in range(n)]
a = cons_matr(n)
s = [i+1 for i in range(n**2)]
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
di = 0
dj = 0
for i in range(n):
	if c[0][-1] != 0:
		c = revmatr(transpmatr((c)))
		di += 1
		i -= di
	for j in range(n):
		prmatr(c)
		print(s)
		print(i, j, c[i][j], di,dj)
		if c[i][j] == 0:
			c[i][j] = s[n*(i+di)+j-dj]
			s[n*(i+di)+j-dj] = 0
		else:
			dj += 1
			j-=dj
prmatr(c)# она не работает, рабочая версия в файле spiral.py