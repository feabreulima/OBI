m, n = [int(i) for i in input().split()]

matriz = []

total = 0

for j in range(m):
    num = [int(ii) for ii in input().split()]
    matriz.append(num)

compra = int(input())

for f in range(compra):
    x, y = [int(iii) for iii in input().split()]
    
    if matriz[x-1][y-1] > 0:
        matriz[x-1][y-1] -= 1
        total += 1
        
print(total)