t, p, n = [int(i) for i in input().split()]

par = []
for j in range(p):
    par.append([int(i) for i in input().split()])

impar = []
for j in range(n):
    impar.append([int(i) for i in input().split()])

pessoas = int(t/3)
matriz = []

for j in range(pessoas):
    matriz.append([int(i) for i in input().split()])

rest = x = i = 0
