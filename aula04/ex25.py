numero = int(input('Digite um numero inteiro positivo: '))

unidade = numero % 10
numero = (numero - unidade)/10

dezena = numero % 10
numero = (numero - dezena)/10

centena = numero % 10 
numero = (numero - centena)/10

milhar = numero

dezena = int(dezena)
centena = int(centena)
milhar = int(milhar)
print(milhar, 'milhar(s)', centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)')