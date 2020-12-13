from math import hypot

catOposto = float(input('Digite o cateto oposto: '))
catAdj = float(input('Digite o cateto adjacente: '))
hip = hypot(catOposto, catAdj)
print(f'O comprimento da Hipotenusa é {hip:.2f}')
