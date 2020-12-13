from random import random, randint
from time import sleep

nRandom = randint(0,10)
num = int(input('Digite um número entre 0 e 10: '))
vezes = 0

if (num == nRandom):
    print('Parabens')
    vezes += 1

while num != nRandom:
    num = int(input(f'Você errou, tente outra vez: '))
    vezes += 1
    
    if (num == nRandom):
        print('Parabens')
        vezes += 1
        
print(f'Você tentou {vezes} vez(es) até conseguir.')
