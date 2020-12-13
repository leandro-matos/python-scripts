times = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Grêmio', 'Fluminense',
	     'Internacional', 'Palmeiras', 'Santos', 'Ceará', 'Fortaleza',
         'Corinthians', 'Athletico-PR', 'Bahia', 'Bragantino', 'Atlético-GO',
         'Sport', 'Vasco', 'Coritiba', 'Botafogo', 'Goiás')

print(f'\nLista de times do Brasileirão: {times}')
print(f'\nOs cinco primeiros colocados: {times[0:5]}')
print(f'\nOs últimos quatro colocados: {times[16:20]}')
print(f'\nTimes em ordem alfabética: {sorted(times)}')
posicao = times.index('Palmeiras') + 1
print(f'\nO Palmeiras está na {posicao}º posição')