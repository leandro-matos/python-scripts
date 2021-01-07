try:
    with open('arquivo.txt') as file:
        print('Arquivo aberto com sucesso')
except Exception as err:
    print('Falha ao abrir o arquivo')
    print(err)

