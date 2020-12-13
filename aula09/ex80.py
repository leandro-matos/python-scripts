listapalavras = ('almocar', 'jantar', 'dormir', 'acordar', 'estudar', 'sentar', 'cozinhar')

for p in listapalavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('')