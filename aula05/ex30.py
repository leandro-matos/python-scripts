from random import random, randint
from time import sleep
nRandom = randint(0,5)
print('-=-' * 20)
num = int(input('Digite um número entre 0 e 5: '))
print('Analisando...')
sleep(2)
if (num == nRandom):
    print('Parabens, Você Venceu')
elif (num <0 or num >6):
    print('Você digitou um número fora dos padrões')
else:
    print(f'Você perdeu, o número randômico é o {nRandom}')
print('-=-' * 20)
