from datetime import date
data = date.today()
anoAtual = data.year
ano = int(input('Digite o ano de nascimento do atleta: '))
categoriaDif = anoAtual - ano

if categoriaDif <=9:
    print(f'Você tem {categoriaDif} anos, sua categoria: MIRIM')
elif categoriaDif <=14:
    print(f'Você tem {categoriaDif} anos, sua categoria: INFANTIL')
elif categoriaDif <=19:
    print(f'Você tem {categoriaDif} anos, sua categoria: JUNIOR')
elif categoriaDif <=20:
    print(f'Você tem {categoriaDif} anos, sua categoria: SÊNIOR')
else:
    print(f'Você tem {categoriaDif} anos, sua categoria: MASTER')