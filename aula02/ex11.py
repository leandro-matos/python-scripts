valor = float(input("Quanto dinheiro você tem na carteira ? R$ "))
valorDolar = valor / 5.32
valorEuro = valor / 6.34
print(f'Com {valor} você pode comprar US${valorDolar:.2f}')
print(f'Com {valor} você pode comprar €${valorEuro:.2f}')