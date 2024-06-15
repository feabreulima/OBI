n = int(input())
m = int(input())
s = int(input())

total = cont = 0

S_numeros = []
# deve estar entre n e m. a soma dos dígitos de I é igual a s.

for i in range(n,m+1):
    
    str_I = str(i) # ex: '234'
    
    for ii in range(len(str_I)): # quebrando str de dígito por dígito
        total += int(str_I[ii])
        
    if total == s: #em caso positivo
            S_numeros.append(i)
            
    total = 0

M_S_numeros = sorted(S_numeros)

if len(S_numeros) > 0:
    print(M_S_numeros[-1])
else:
    print("-1")
