cardapio = ['Carne', 'Queijo', 'Frango', 'Calabresa']
vendas = []

for indice, elemento in enumerate(cardapio):
    print(f'[{indice}]: {elemento}')

print()
try:   
    opcao = int(input('Digite o Sabor Desejado: '))
    print('O sabor escolhido foi: ', cardapio[opcao])
except:
    print('Opção Inválida')