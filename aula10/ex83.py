pessoas = list()
dado = list()
resp = 'S'
maior = men = 0
while resp in 'Ss':
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    
    if len(pessoas) == 0:
        maior = men = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
            
        if dado[1] < men:
            men = dado[1]
            
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input('Quer Continuar? (S/N) ')).upper().strip()

print('')
print('Lista de Pessoas: ', end='')
for p in pessoas:
    print(f'{p[0]}, ', end='')
    
print(f'\nQuantidade de pessoas: {len(pessoas)}')

print(f'\nMaior peso: {maior} kg. Peso de: ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'{pessoa[0]} ', end='')

print(f'\nMenor peso: {men} kg. Peso de: ', end='')
for pessoa in pessoas:
    if pessoa[1] == men:
        print(f'{pessoa[0]} ', end='')