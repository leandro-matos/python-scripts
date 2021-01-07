
def mensagem_boasvindas(nome):
    print(f'Seja bem Vindo ao {nome}')
    
mensagem_boasvindas(nome='Devops')
mensagem_boasvindas(nome='FullStack')

def add_pedidos(cliente, sabor):
    if len(cliente) < 1:
        msg_err = 'Insira o nome do cliente'
        return msg_err
    else:
        novo_pedido = f'O {cliente} pediu pastel de {sabor}'
        return novo_pedido

pedido1 = add_pedidos('Leandro', 'Queijo')
print(pedido1)

pedido2 = add_pedidos('', 'Carne')
print(pedido2)