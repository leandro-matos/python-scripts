print('--'*20)
print('Exercício 01')
print('')

num = input('Número: ')
try:
    num = int(num)
    if num > 0:
        if num % 2 == 0:
            print(f'{num} é Par')
        else:
            print(f'{num} é Impar')
    else:
        print('Digite um número inteiro !')
except:
    print('Digite apenas números')

print('')
print('--'*20)
print('Exercício 02')
hora = input('Digite a hora do dia: (0-23): ')
try:
    hora = int(hora)
    if hora >=0 and hora<=11:
        print(f'Bom dia, são {hora} horas. ')
    elif hora >=12 and hora <=17:
        print(f'Boa tarde, são {hora} horas. ')
    elif hora >=18 and hora <=23:
        print(f'Boa noite, são {hora} horas')
    else:
        print('Hora Inválida, somente de 0 a 23.')
except:
    print('Digite apenas números')

print('--'*20)
print('Exercício 03')
print('')
nome = (input('Nome: ')).strip()
tam = len(nome)
print(f'Seu nome tem {tam} letras')
