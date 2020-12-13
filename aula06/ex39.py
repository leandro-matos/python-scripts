num = int(input('Digite um número para conversão: '))
print('01 - binário, 02 para octal, 03 para hexadecimal ')
escolha = int(input('Escolha uma opção para a conversão: '))
print('')

if escolha == 1:
    print(f'Número em binário: {bin(num)[2:]}')
elif escolha == 2:
    print(f'Número em Octal: {oct(num)[2:]}')
elif escolha == 3:
    print(f'Número em Hexa: {hex(num)[2:]}')
else:
    print('Opção inválida')