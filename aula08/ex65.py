n1 = int(input('Digite o numero: '))
fat = n1
mult = 1
while fat >= 1:
    mult = mult * fat
    fat -= 1
    
print(f'Fatorial de {n1} é: {mult}')
    