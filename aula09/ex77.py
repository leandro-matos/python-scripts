from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
    
print(f'\nO maior valor sorteado: {max(numeros)}')
print(f'O menor valor sorteado: {min(numeros)}')