import csv

print('Leitura de Arquivo CSV')
file = open('menu.csv', 'r')
file_csv = csv.reader(file, delimiter=';')
for [sabor, valor, status] in file_csv:
    print(f'O pastel {sabor}, custa {valor} e seu status está: {status}')
file.close()
print()

print('Escrita em arquivo CSV')
create_file = open('pedidos.csv', 'w', newline='', encoding='utf-8')
write = csv.writer(create_file, delimiter=';')
header = ['ID', 'CLIENTE', 'VALOR']
write.writerow(header)

pedido1 = ['01', 'Leandro', '10']
pedido2 = ['02', 'Maria', '100']
print('Pedidos Adicionados com sucesso')
write.writerow(pedido1)
write.writerow(pedido2)

create_file.close()