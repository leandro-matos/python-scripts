lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

for comida in lanche:
    print(comida)
print('\n')
for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')
print('\n')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('\n')

print(sorted(lanche))
print(lanche)