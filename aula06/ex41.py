from datetime import date
data = date.today()
anoAtual = data.year
ano = int(input('Digite o ano de nascimento: '))
idade = anoAtual - ano
anoAlistamento = ano + 18


if idade < 18:
    print(f'Quem nasceu em {ano} tem {idade} anos em {anoAtual}.')
    print(f'Ainda faltam {18 - idade} ano(s) para o alistamento.')
    print(f'Seu alistamento será em {anoAlistamento}. ')
elif idade > 18:
    print(f'Quem nasceu em {ano} tem {idade} anos em {anoAtual}.')
    print(f'Você já deveria ter se alistado há {anoAtual - anoAlistamento} anos.')
    print(f'Seu alistamento foi em {anoAlistamento}.')
else:
    print(f'Quem nasceu em {ano} tem {idade} anos em {anoAtual}.')
    print('Você deve se alistar imediatamente !! .')