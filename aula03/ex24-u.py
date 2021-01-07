import json

with open('meus_pedidos.json') as file:
    json_data = json.load(file)
    
print(type(json_data))
print(json_data)
print()

json_data_dumps = json.dumps(json_data)
print(type(json_data_dumps))
print(json_data_dumps)
print()

json_string = '{"estabelecimento": "Pedidos Devops", "pedidos": [{"cliente": "Leandro", "valor": 25.0}, {"cliente": "Marcos", "valor": 55.0}]}'
print(json_string)
print(type(json_string))
print()

json_data_s = json_string = json.loads(json_string)
print(json_data_s)
print(type(json_data_s))