n = int(input())
vetor = [int(x) for x in input().split()]

cont = l = 0
r = n-1

sl = vetor[l]
sr = vetor[r]

while l <= r:
    if vetor[l] == vetor[r]:
        l += 1
        r -= 1
        
        sl = vetor[l]
        sr = vetor[r]
        
    elif sl > sr:
        l += 1
        sl += vetor[l]
        cont += 1
        if l == r:
            break
    elif sr > sl:
        r -= 1
        sr += vetor[r]
        cont += 1
        if l == r:
            break
print(cont)