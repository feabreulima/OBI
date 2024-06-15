dominante = input()

luana = edu = 0

figuras = [10,11,12,13]

for i in range(3):
    cartas = input()
    if cartas[0] == 'A':
        luana += 10
        
    elif cartas[0] == 'J':
        luana += 11
        
    elif cartas[0] == 'Q':
        luana += 12
        
    elif cartas[0] == 'K':
        luana += 13
        
    if cartas[1] == dominante[1]:
        luana += 4
        
for i in range(3):
    cartas = input()
    if cartas[0] == 'A':
        edu += 10
        
    elif cartas[0] == 'J':
        edu += 11
        
    elif cartas[0] == 'Q':
        edu += 12
        
    elif cartas[0] == 'K':
        edu += 13
        
    if cartas[1] == dominante[1]:
        edu += 4
        
if edu > luana:
    print('Edu')
elif luana > edu:
    print('Luana')
else:
    print('empate')