n,q = [int(i) for i in input().split()]

indiceX = 0

l = [0 for i in range(n)]
matriz = [l.copy() for i in range(n)]

for i in range(n):
  valores = [char for char in input()]

  for j in valores:
      matriz[i][indiceX] = int(j)
      indiceX += 1
      
  indiceX = 0    
    
for i in range(n):  print(f'{matriz[i]}')