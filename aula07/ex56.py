n = int(input('Digite um número: '))
nprimo = 0
for count in range (1, n+1):
    if n % count == 0:
        nprimo += 1
if nprimo == 2:
    print(f'O número {n} é um número primo')
else:
    print(f'O número {n} não é um número primo')