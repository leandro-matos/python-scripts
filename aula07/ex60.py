soma = 0
contador = 0
idadeVelho = 0
nomeVelho = None
idadeMulher = 0

for p in range(1, 5):
    print(f'\n---------- {p}° pessoa --------')
    nome = str(input(f'Digite o nome da Pessoa nº {p}º: '))
    idade = int(input(f'Digite a idade da Pessoa nº {p}º: '))
    sexo = str(input(f'Digite o sexo da Pessoa nº {p}º (M ou F): ')).strip().upper()
    
    soma += idade
    contador += 1
    
    if p == 1 and sexo == 'M':
        idadeVelho = idade
        nomeVelho = nome
    if sexo == 'M':
        if idade > idadeVelho:
            nomeVelho = nome   
    
    if sexo == 'F':
        if idade < 20:
            idadeMulher +=1
                 
print('')
print(f'Média de idade do grupo: {soma/contador:.1f} ano(s)')
print(f'O nome do mais velho é: {nomeVelho}')
print(f'Qtd de mulheres com menos de 20 anos: {idadeMulher}')
