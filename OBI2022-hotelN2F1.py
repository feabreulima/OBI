d = int(input()) # valor diária dia 1
a = int(input()) # valor aumentos a partir dia 2
n = int(input()) # dia da chegada

total = diaria = 0

if n == 1:
    total = d*31

elif n > 1 and n < 16:
    diaria = d+((n-1)*a)
    total = ((31-(n-1))*diaria)

elif n >= 16:
    diaria = d+((15-1)*a)
    total = ((31-(n-1))*diaria)
    
print(total)