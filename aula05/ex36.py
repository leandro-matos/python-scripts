salario = float(input('Digite o salário: '))

if salario <=0:
    print('Informe um salário válido.')
elif salario > 1250:
    aumento = salario + (salario * 0.10)
    print(f'Seu salário era de: R$ {salario:.2f}, agora o seu salário é de: R$ {aumento:.2f}')
else:
    aumento = salario + (salario * 0.15)
    print(f'Seu salário era de: R$ {salario:.2f}, agora o seu salário é de: R$ {aumento:.2f}')    