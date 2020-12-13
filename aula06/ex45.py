peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura * altura)

if peso <=0 or altura <=0:
    print('Calcule novamente e informe os dados corretamente (peso e altura)')
elif imc < 18.5:
    print(f'O seu IMC é {imc:.2f}, você está abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print(f'O seu IMC é {imc:.2f}, você está no peso ideal')
elif imc >= 25 and imc <= 29.9:
    print(f'O seu IMC é {imc:.2f}, você está com sobrepeso')
elif imc >= 30 and imc <= 39.9:
    print(f'O seu IMC é {imc:.2f}, você está com obesidade')
else:
    print(f'O seu IMC é {imc:.2f}, você está com obesidade mórbida')


