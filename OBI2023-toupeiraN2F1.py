s, t = [int(i) for i in input().split()] #s: nro salões; t: nro túneis

linha = [0 for i in range(s)]

matriz = [linha.copy() for i in range(s)] # matriz das adjacências

for i in range(t):  # colocando "1" nas matrizes adjacentes
    x, y = [int(i) for i in input().split()]
    matriz[x-1][y-1] = 1
    matriz[y-1][x-1] = 1 # a adjacência é simétrica

n_SugestoesPasseio = int(input()) # nro de passeios

total = n_SugestoesPasseio

for i in range(n_SugestoesPasseio):  # pegando cada lista com o nro de sugestoes de passeio
    possiveisTuneis = [int(i) for i in input().split()]
    nova = possiveisTuneis[1:].copy()
    
    for i in range(1, len(nova)):  # ou for in range(1,len(nova)):; com índices nova[i-1]
        if matriz[nova[i-1]-1][nova[i]-1] != 1:
            total -= 1
            break
        
print(total)