pessoas = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()

for p in pessoas:
    if p[1] >= 21:
        totmaior += 1
        print(f'Maior de idade: {p[0]}')
    else:
        totmenor +=1
        print(f'Menor de idade: {p[0]}')
print('')
print(f'Total Maior de idade: {totmaior}')
print(f'Total Menor de Idade: {totmenor}')