pedidos_segunda = [
    {'cliente': 'José', 'pastel': 'Queijo'},
    {'cliente': 'José', 'pastel': 'Carne'},
    {'cliente': 'Pedro', 'pastel': 'Queijo'},
    {'cliente': 'Carlos', 'pastel': 'Carne'},
    {'cliente': 'José', 'pastel': 'Queijo'},
]

pedidos_terca = [
    {'cliente': 'Marcos', 'pastel': 'Queijo'},
    {'cliente': 'Daniel', 'pastel': 'Carne'},
    {'cliente': 'Pedro', 'pastel': 'Queijo'},
    {'cliente': 'Carlos', 'pastel': 'Carne'},
    {'cliente': 'Lucas', 'pastel': 'Queijo'},
]


clientes_segunda = set()
for pedido in pedidos_segunda:
    clientes_segunda.add(pedido['cliente'])
print(f'Segunda: {clientes_segunda}')

clientes_terca = set()
for pedido in pedidos_terca:
    clientes_terca.add(pedido['cliente'])
print(f'Terça: {clientes_terca}')

todos_clientes = clientes_segunda | clientes_terca
print(f'União: {todos_clientes}')

clientes_compra = clientes_segunda.intersection(clientes_terca)
print(f'Interseção: {clientes_compra}')

clientes_diferenca = clientes_segunda - clientes_terca
print(f'Diferença: {clientes_diferenca}')