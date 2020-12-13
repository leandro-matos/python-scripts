num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))


print('')
print(f'Lista de Números: {num};')                   
print(f'O valor 9 aparece {num.count(9)} vezes;')

if 3 in num:
       posicao = num.index(3) + 1
       print(f'O valor 3 apareceu na {posicao}° posição;')
else:
       print(f'O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end=' ')
for n in num:
       if n % 2 == 0:
              print(n, end= ' ')
