while True:
    print()
    n1 = input('N1: ')
    n2 = input('N2: ')
    op = input('Operador: ')
    
    if not n1.isnumeric() or not n2.isnumeric():
        print('Digite apenas números')
        continue

    n1 = int(n1)
    n2 = int(n2)
    
    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '*':
        print(n1 * n2)
    else:
        print('Operação Inválida')
    print()
    sair = input('Deseja sair ? ').strip()
    if sair == 'S':
        break