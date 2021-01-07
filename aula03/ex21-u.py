file = open('pedidos.txt')
pedidos = file.readlines()
for pedido in pedidos:
    print(pedido.replace('\n', ''))
file.close()
   
print('') 
clientes = ['José', 'Carlos', 'Lucas', 'Pedro', 'Jacksn']
file = open('clientes.txt', 'w')
for cliente in clientes:
    print(f'Cliente: {cliente} adicionado na lista.')
    file.write(f'{cliente}\n')
file.close()