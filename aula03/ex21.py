import random

aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))

alunoList = [aluno1,aluno2,aluno3,aluno4]
print("Lista Digitada:", alunoList)

random.shuffle(alunoList)
print("Ordem de Apresentação dos Alunos:", alunoList)
