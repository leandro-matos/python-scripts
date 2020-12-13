valorCasa = float(input('Informe o valor da casa: '))
salario = float(input('informe o salário do comprador: '))
ano = int(input('Informe a quantidade de anos que pretende pagar: '))

prestacao = valorCasa / (ano * 12)
emprestimo = (salario * 0.30);

if prestacao <= emprestimo:
    print(f'O empréstimo será concedido. Você terá de pagar R$ {prestacao:.2f}')
else:
    print(f'O empréstimo será negado. O valor de R$ {prestacao:.2f} supera o que você pode pagar')
