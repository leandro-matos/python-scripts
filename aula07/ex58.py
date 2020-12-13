from datetime import date
data = date.today()
anoAtual = data.year

somaMaior = 0
somaMenor = 0
for count in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da Pessoa nº {count}º: '))
    idade = anoAtual - ano
    if idade >= 18:
        somaMaior += 1
    else:
        somaMenor += 1
print(f'Maiores de Idade: {somaMaior}')
print(f'Menores de Idade: {somaMenor}')
