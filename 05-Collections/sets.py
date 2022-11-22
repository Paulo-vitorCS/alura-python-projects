# Trabalhando com conjuntos (sets):

conjunto1 = {10, 15, 20, 25}
conjunto2 = {5, 15, 18, 25}

# Uma lista pode ser transformada em um conjunto usando set:
lista = [1, 2, 3]
conjunto = set(lista)
print(f'Lista: {lista} vs Conjunto: {conjunto}')

# Comparando conjuntos (OU -> |):
# Os elementos que pertencem à um conjunto ou outro
conjunto3 = conjunto1 | conjunto2
print(conjunto3)

# Comparando conjuntos (E -> &):
# Somente os elementos que pertencem aos dois conjuntos
conjunto4 = conjunto1 & conjunto2
print(conjunto4)

# Comparando conjuntos (OU exclusivo -> -):
# Somente os elementos que pertencem ao primeiro conjunto, mas não ao segundo
conjunto5 = conjunto1 - conjunto2
print(conjunto5)

# Tamanho do conjunto:
print(f'Tamanho do conjunto: {len(conjunto)}')

# Adicionando elementos ao conjunto:
conjunto.add(4)
print(f'Conjunto com adição do 4: {conjunto}')

# Conjunto congelado (frozenset) não pode receber novos elementos
conjunto_cong = frozenset(conjunto)
print(f'Conjunto congelado: {conjunto_cong}')
