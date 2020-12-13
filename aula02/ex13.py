preco = float(input('Qual é o preço do produto ? R$ '))
precoDesc = preco - (preco * 5/100)
print(f'O produto que custava {preco}, na promoção com desconto de 5% vai custar {precoDesc:.2f}')