cardapio = {}
print(type(cardapio))

pastel = {'sabor': 'queijo', 'valor': 6.00, 'status': True}
print(pastel)

print(pastel['sabor'])
pastel['valor'] = 7.00
print(pastel)

pastel['quantidade'] = 10
print(pastel)

values = pastel.values()
print(values)
for value in values:
    print(f'O elemento {value} está no dicionário')

dict_values = pastel.items()
print(dict_values)
for info in dict_values:
    print(info, type(info))