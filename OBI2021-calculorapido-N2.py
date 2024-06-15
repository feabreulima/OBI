S = int(input())
A = int(input())
B = int(input())

soma = total = 0

for x in range(A,B+1):
    i = str(x)
    for k in i:
        K = int(k)
        soma += K
        
    if soma == S:
        total += 1
    else:
        soma = 0
        

print(total)