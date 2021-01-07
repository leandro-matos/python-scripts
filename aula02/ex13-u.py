string = 'Leandro de Matos Pereira'
valor = 5

print(string.replace('Leandro', 'Fernanda'))
print(string.upper())
print(string.lower())
print(string.startswith('Leandro'))
print(string.endswith('Matos'))
print(f'Quantidade de caracteres:', len(string))
print('Primeiro Caractere: ', string[0])
print('Último Caractere: ', string[-1])
print('Caracteres no meio:', string[5:15])

result = 'Matos' in string 
print(result)
print()

print('Concatenação')
print('String ' + string)
print()

print('Interpolação: ')
print('String : %s ' %string)
print()

print('Método Format')
print('String: {}'.format(string))
print()

print('Método Fstring')
print(f'String: {string}, valor: {valor:.2f}')
