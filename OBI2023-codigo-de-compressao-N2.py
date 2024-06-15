j = int(input())
cod = input()
x = 0
y = total = cont = 1

while cont < j:
    if cod[x] == cod[y]:
        total += 1
    else:
        print(f'{total} {cod[x]}', end=' ')
        total = 1
    x += 1
    y += 1
    cont += 1
print(f'{total} {cod[x]}')