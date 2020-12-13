frase = str(input('Digite a sua frase: ')).upper().strip()
letra = frase.count('A')
primeira = frase.find('A') + 1
ultima = frase.rfind('A') + 1
print(f'Quantas vezes aparece a letra A: {letra}')
print(f'Primeira Posição: {primeira}')
print(f'Última Posição: {ultima}')
