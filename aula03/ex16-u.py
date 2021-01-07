cardapio = ['carne', 'pizza', 'queijo', 'coxinha', 'pastel']

for elemento in cardapio:
    print(elemento)

print()
npar = []
nimpar = []
numeros = range(1, 21)
for numero in numeros:
    if numero % 2 == 0:
        npar.append(numero)
    else:
        nimpar.append(numero)

print('Números   Pares: ', npar)
print('Números Impares: ', nimpar)