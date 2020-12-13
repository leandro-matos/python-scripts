from math import radians, cos, tan, sin

angulo = float(input('Digite o ângulo: '))
se = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'Seno: {se:.2f}, Cosseno: {cosseno:.2f}, Tangente: {tangente:.2f}')