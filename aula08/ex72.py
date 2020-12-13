resp = 'S'
soma = media = maior = menor = 0
count = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    count += 1
    if count ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer Continuar? (S/N) ')).upper().strip()
media = soma / count

print('--'*20)
print(f'Quantidade de valores: {count}')
print(f'Soma dos valores: {soma}')
print(f'Média dos valores: {media}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print('--'*20)