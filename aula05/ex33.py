distancia = float(input('Digite a distância de uma viagem em KM: '))

if distancia < 1 :
    print('Digite uma distância válida')
elif distancia >= 200:
    valor = distancia * 0.45;
    print(f'O preço da sua viagem: {valor:.2f}');
else:
    valor = distancia * 0.50;
    print(f'O preço da sua viagem: {valor:.2f}');