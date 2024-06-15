Ia, Ib, Fa, Fb = [int(i) for i in input().split()]

total = 0

while Ia != Fa or Ib != Fb: 
    if Ib != Fb:
        Ib = Fb
        if Ia == 0:
            Ia = 1
            total += 1
        else:
            Ia = 0
            total += 1
        if Ia != Fa:
            Ia = Fa
            total += 1
    else:
        if Ia != Fa:
            Ia = Fa
            total +=1
print(total)
