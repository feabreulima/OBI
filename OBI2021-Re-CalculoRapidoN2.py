S = int(input())
A = int(input())
B = int(input())

total = soma = 0

for i in range(A,B+1):
    x = str(i)
    for k in x:
        y = int(k)
        soma += y
    if soma == S:
        total += 1
    soma = 0
print(total)