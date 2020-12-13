soma = 0
contador = 0
for numero in range(1, 501):
    if numero % 2 != 0:
        if numero % 3  == 0:
            soma += numero
            contador += 1

print(f'A soma de todos os {contador} valores solicitados é {soma}')