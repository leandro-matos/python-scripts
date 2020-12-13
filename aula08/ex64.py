n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print(' \n [1] Somar\n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do Programa')
    opcao = int(input('\nQual a opção? '))
    
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1:.1f} + {n2:.1f} é: {soma:.1f}')
    elif opcao == 2:
        multiplica = n1 * n2
        print(f'A multiplicação de {n1:.1f} * {n2:.1f} é: {multiplica:.1f}')
    elif opcao ==3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n2 > n1:
            print(f'O maior número é {n2}')
        else:
            print('Números iguais')
    elif opcao == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opcao > 5:
        print('\nOpção Inválida, escolhe um número de 1 a 5')