for numero in range(1, 11, 3):
    print(numero)

nome = 'Leandro de Matos Pereira'
nome2 = ''

for letra in nome:
    if letra == 'L' or letra =='M' or letra =='P':
        nome2 = nome2 + letra.lower()
    else:
        nome2 += letra
print(nome)
print(nome2)