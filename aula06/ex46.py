print('BEM VINDO A LOJA !')
print('')
preco = float(input('Digite o valor do produto: '))
print('')
escolha = int(input('Escolha a forma de Pagamento: \n 1) A vista no dinheiro/cheque \n 2) A vista no cartão \n 3) Em até 2x no cartão \n 4) 3x ou mais no cartão\n\n Infome a opção: '))
print('')
if escolha == 1:
    valor = preco - (preco * 10/100)
    print(f'Preço Antigo: {preco:.2f}, Novo valor: {valor:.2f}')
elif escolha == 2:
    valor = preco - (preco * 5/100)
    print(f'Preço Antigo: {preco:.2f}, Novo valor: {valor:.2f}')
elif escolha == 3:
    print(f'Preço do produto: {preco}')
elif escolha == 4:
    parcela = int(input('Quantas parcelas: '))
    valor = preco + (preco * 20/100)
    print(f'\nPreço do Produto: {preco:.2f}. \nSua compra será parcela em {parcela:.0f}x de {valor/parcela:.2f}. Novo valor: {valor:.2f}')
else:
    print('Opção Inválida, execute novamente.')