# Trabalhando com dicionários (também conhecidos como mapas):

produtos = {
    'produto 1': 10,
    'produto 2': 15,
    'produto 3': 20
}

print(produtos)

# Acessando um valor específico, dada a chave
print(produtos['produto 2'])

# É possível fazer uma consulta de forma a não retornar erro, casa a chave não esteja no dicionário:
# Caso a chave esteja no dicionário, retorne, caso contrário retorne 0
print(produtos.get('produto 4', 0))

# Atribuindo novas chaves e valores para o dicionário já existente:
produtos['produto 4'] = 25
print(produtos)

# Apagando elementos:
del produtos['produto 3']
print(produtos, '\n')

# Usando laços para impressão das chaves:
for chave in produtos:
    print(chave)

# Usando laços para impressão dos valores:
for valor in produtos.values():
    print(valor)

# Usando laços para impressão dos items do dicionário:
for item in produtos.items():
    print(item)

for chave, valor in produtos.items():
    print(f'Chave: {chave} | Valor: {valor}')
