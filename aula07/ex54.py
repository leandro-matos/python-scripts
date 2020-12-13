soma = 0
for count in range(1, 7):
    n = int(input(f'Digite o {count}º valor: '))
    if n % 2 == 0:
        soma += n
if soma > 0:
    print(f'A soma de todos os valores pares foi {soma}')
else:
    print('Você digitou apenas valores ìmpares, não foi computada a soma.')