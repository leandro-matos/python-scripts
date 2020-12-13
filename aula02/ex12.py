largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
litros = (largura * altura) * 0.5
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {litros}l de tinta.')