cardapio = ['Carne', 'Queijo', 'Frango', 'Calabresa']
vendas = []

print(cardapio)
print(f'Tamanho da Lista: {len(cardapio)}')
print(f'Primeiro Elemento: {cardapio[0]}')
print(f'Último Elemento: {cardapio[-1]}')
print()

print('Adicionando novos Elementos:')
cardapio.append('Coxinha')
print(cardapio)
print()

print('Acessando Trechos da Lista:')
print(cardapio[1:3])
print(cardapio[3:])
print(cardapio[:2])
print()

print('Organizando uma lista')
print(sorted(cardapio, key=str.lower))
print()

print('Removendo Elementos')
cardapio.remove('Coxinha')
print(cardapio)
print()

print('Quantidade de Elementos: ')
print(f'Quantidade de Carne: {cardapio.count("Carne")}')

print('Inserindo novos elementos')
cardapio.insert(0, 'Palmito')
cardapio.insert(1, 'Pizza')
print(cardapio)
print()

print('Excluindo elementos da lista')
cardapio.pop(4)
del cardapio[3:]
print(cardapio)

print()
vendas.append(10)
vendas.append(20)
vendas.append(30)
vendas.append(40)
print('Valor Máximo:', max(vendas))
print('Valor Mínimo:', min(vendas))
print('Soma de Valores: ', sum(vendas))
print(f'Média de Valores: {sum(vendas)/len(vendas):.2f}')
print()

numeros = list(range(1, 31))
print(numeros)
print('Quantidade de Números: ', len(numeros))
del numeros[:10]
print('Removendo 10 primeiros números: ', numeros)