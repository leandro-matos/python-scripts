from random import choice

aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))

listaAlunos = [aluno1,aluno2,aluno3,aluno4]

print(f'O aluno sorteado foi: {choice(listaAlunos)}')