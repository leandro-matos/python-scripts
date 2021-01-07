import json

meus_pedidos = {
    "estabelecimento": "Pedidos Devops",
    "pedidos": [
        {
            "cliente": "Leandro",
            "valor": 25.00
        },
                {
            "cliente": "Marcos",
            "valor": 55.00
        },
    ]
}

json_data = json.dumps(meus_pedidos, indent=4)
print(json_data)
print()

print('Serialização Finalizada')
with open('meus_pedidos.json', 'w') as file:
    json.dump(meus_pedidos, file, indent=4)


