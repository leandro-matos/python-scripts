n = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão aritmética: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end= ' > ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais: '))
print('FIM')