val = float(input("Digite o valor em metros: "))
cen = val * 100
mil = val * 1000
dam = val / 10
hm = val / 100
km = val / 1000
print(f'Valor em centimentros {cen:.0f}cm em milimetros {mil:.0f}mm')
print(f'Valor em dam {dam} em hm {hm}')
print(f'Valor em km {km}')