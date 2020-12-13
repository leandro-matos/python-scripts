maiorPeso = 0
menorPeso = 0
for count in range(1, 6):
    peso = float(input(f'Digite o peso da Pessoa nº {count}º: '))
    
    if count == 1:
        maiorPeso = peso
        menorPeso = peso
        
    if peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso   
          
print(f'Maior Peso: {maiorPeso}')
print(f'Menor Peso: {menorPeso}')