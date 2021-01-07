nome = input('Nome: ')
idade = int(input('Idade: '))

idade_menor = 18
idade_maior = 30

if (idade >= idade_menor and idade <= idade_maior):
    print(f'{nome}, você pode pegar o empréstimo')
else:
    print(f'{nome}, você não pode pegar o empréstimo')