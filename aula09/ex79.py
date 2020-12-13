listaprod = ('Caneta', 1.50, 'Lápis', 1.0, 'Borracha', 0.50, 'Apontador', 2.50)

print('-'*30)
print(f'{"LISTA DE PREÇOS":^25}')
print('-'*30)
for cont in range(0, len(listaprod)):
    if cont % 2 == 0: 
        print(f'{listaprod[cont]:.<20}', end='')
    else:
        print(f'R${listaprod[cont]:>6.2f}')
