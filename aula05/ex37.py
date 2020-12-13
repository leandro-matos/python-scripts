from time import sleep
r1 = float(input('Digite a r1: '))
r2 = float(input('Digite a r2: '))
r3 = float(input('Digite a r3: '))
print('Analisando...')
sleep(1)
if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
    print('Nao é um triangulo')
else:
    print('\033[1;É um triângulo')
