soma = cont = n = 0

while n != 999:
    n = int(input('Digite um número: [999 para parar]: '))
    if n != 999:
        cont += 1
        soma += n
print(f'Quantidade de números digitados {cont}, soma dos valores {soma}')