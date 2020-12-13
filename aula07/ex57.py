palavra = str(input('Digite a frase: ')).upper().strip().replace(' ', '')

if palavra == palavra[::-1]:
    print('Palindromo')
else:
    print('Não é um palindromo')
