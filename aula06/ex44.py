from time import sleep
r1 = float(input('Digite a r1: '))
r2 = float(input('Digite a r2: '))
r3 = float(input('Digite a r3: '))
print('Analisando...')
sleep(1)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É um triângulo')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 !=r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Não é um triângulo')