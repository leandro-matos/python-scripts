n = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão aritmética: '))
termo = n
cont = 1

while cont <= 10:
    print(termo, end= ' > ')
    termo += razao
    cont += 1
    
print('FINISH')

    