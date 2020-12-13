n = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = n + (10 - 1) * razao
for c in range(n, decimo + razao , razao):
        print(c, end=' -> ')
print('ACABOU')