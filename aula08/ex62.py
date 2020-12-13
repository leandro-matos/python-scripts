sexo = '0'
while sexo != 'M' and sexo !='F':
    sexo = str(input('Informe o seu sexo: ')).upper().strip()
    
    if sexo == 'M' or sexo =='F':
        print('Parabens, você tem um sexo.')
    else:
        print('Dados inválidos')