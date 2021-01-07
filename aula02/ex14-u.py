status = 1
while status == 1:
    pedido = input('Sabor do Pastel: ')
    print('Item Confirmado')
    status = int(input('Digite 1 para aceitar, 0 para sair: '))

cont = 0
qtde = 3
while cont < qtde:
    pedido = input('Sabor do Pastel: ')
    print(f'Pedido Confirmado')
    cont += 1