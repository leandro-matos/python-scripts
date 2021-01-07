num1 = input('Num 01: ')
num2 = input('Num 02: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(f'Soma: {num1 + num2}')
except:
    print('Não foi possível efetuar a soma')