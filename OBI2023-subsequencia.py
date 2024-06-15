a, b = [int(i) for i in input().split()]

resp = 'N'
i = j = 0

sa = [int(i) for i in input().split()]
sb = [int(i) for i in input().split()]

for j in sa:
    if j == sb[i]:
        i += 1
    if i == b:
        resp = 'S'
        break
print(resp)