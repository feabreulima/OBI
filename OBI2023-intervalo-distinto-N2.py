j = int(input())
num = []

for i in range(j):
    num.append(int(input()))
print(num)

#começa o código aquii

total = x = 0
y = 1
temp = [num[x]]

for z in num:
    for n in temp:
        if num[y] == n:
            total = len(temp)
            
        if num[y] != temp[-1] and n == temp[-1]:
            temp.append(num[y])
    y += 1
    