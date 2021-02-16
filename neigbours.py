list = [[int(i) for i in input().split()]]
r = input().split()
if r != ['end']:
	add=[[int(j) for j in r]]
	while add != 'end':
		list.extend(add)
		r = input().split()
		if r != ['end']:
			add=[[int(j) for j in r]]
		else:
			break
m=len(list)
n=len(list[0])
neigh = [[0 for o in range(n)] for u in range(m)]
if n == 1 and m==1:
	neigh=[[(list[0][0])*4]]
	print(neigh[0][0])
elif m == 1 and n!=1:
	neigh[0][0]=(list[0][0])*2+list[0][1]+list[0][n-1]
	neigh[0][n-1]=(list[0][n-1])*2+list[0][n-2]+list[0][0]
	for y in range (1,n-1):
		neigh[0][y]=(list[0][y])*2+list[0][y-1]+list[0][y+1]
	print(*neigh[0])
#добавляем соседей в углах матриц
elif m!=1 and n==1:
	neigh[0][0]=(list[0][0])*2+list[1][0]+list[m-1][0]
	neigh[m-1][0]=(list[m-1][0])*2+list[m-2][0]+list[0][0]
	for y in range (1,m-1):
		neigh[y][0]=(list[y][0])*2+list[y-1][0]+list[y+1][0]
	for g in range(m):
		print(neigh[g][0])
else:
	neigh[0][0]=list[0][1]+list[1][0]+list[0][n-1]+list[m-1][0]
	neigh[0][n-1]=list[0][n-2]+list[1][n-1]+list[m-1][n-1]+list[0][0]#работает
	neigh[m-1][n-1]=list[m-1][n-2]+list[m-2][n-1]+list[0][n-1]+list[m-1][0]#работает
	neigh[m-1][0]=list[m-2][0]+list[m-1][1]+list[0][0]+list[m-1][n-1]#нормально работает
	#добавим границы кроме углов
	for k in range(1,n-1):
		neigh[0][k]=list[0][k-1]+list[0][k+1]+list[1][k]+list[m-1][k]#верхняя граница
		neigh[m-1][k]=list[m-2][k]+list[m-1][k-1]+list[m-1][k+1]+list[0][k]#нижняя граница
	for t in range(1,m-1):
		neigh[t][0]=list[t+1][0]+list[t-1][0]+list[t][1]+list[t][n-1]#левая граница
		neigh[t][n-1]=list[t+1][n-1]+list[t-1][n-1]+list[t][n-2]+list[t][0]#правая граница
	#основная часть матрицы
	l,s = 1,1
	while l<=(m-2):
			s = 1
			while s<=(n-2):
				neigh[l][s]=list[l-1][s]+list[l+1][s]+list[l][s-1]+list[l][s+1]
				s=s+1
			l=l+1
	for p in range(m):
		print(*neigh[p])