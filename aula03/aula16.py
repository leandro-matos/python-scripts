dias = int(input('Quantos dias alugados ?'))
km = float(input('Quantos km ?'))
preco = (dias*60) + (km * 0.15)
print(f'O total à pagar é: {preco:.2f}')