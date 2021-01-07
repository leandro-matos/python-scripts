def imprime_valores(sabor, status='Disponível'):
    print(f'O sabor é {sabor} e o status do pedido {status}')

print('Parametros Opcionais')
imprime_valores('Queijo')
imprime_valores('Frango', 'Indisponivel')
print()

print('Parametros Nomeados')
def imprime_valores_nomeados(valor1, valor2):
    print(f'Valor1 {valor1}, Valor2 {valor2} ')
imprime_valores_nomeados(valor2=2, valor1=1)