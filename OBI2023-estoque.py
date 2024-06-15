m, n = [int(i) for i in input().split()]

total = 0
matriz = []

for y in range(m):
    num = [int(i) for i in input().split()]
    matriz.append(num)
p = int(input())

for j in range(p):
    a, b = [int(i) for i in input().split()]
    if matriz[a-1][b-1] > 0:
        matriz[a-1][b-1] -= 1
        total += 1
print(total)