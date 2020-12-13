velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80:
    acimaVelo = (velocidade - 80) * 7
    print(f"Acima de 80 km. Você deve pagar {acimaVelo:.2f} R$ ")
elif velocidade < 1:
    print('Informe uma velocidade válida')
else:
    print('Dirija com segurança')