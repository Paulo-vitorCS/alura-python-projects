import array as arr
import numpy as np

numeros = arr.array('d', [1.0, 3.5])
print(numeros)

numeros = np.array([1, 3.5])
print(numeros)

numeros += 3
print(numeros, '\n')

idades = [13, 25, 32, 45, 54, 23, 32, 84]

x = list(range(0, len(idades)))  # Forçando a geração de valores
print(x)

y = list(enumerate(idades))  # Utilizando enumerate para gerar uma lista com a posição e o valor
print(y, '\n')

for i in enumerate(idades):
    print(i)

print()

for indice, idade in enumerate(idades):
    print(f'{indice}: {idade}')

print()

usuarios = [
    ('Guilherme', 37, 1981),
    ('Daniel', 25, 1997),
    ('Marcella', 23, 1999)
]

for nome, idade, nascimento in usuarios:  # Desempacontando
    print(nome, end='\t')

print()

for nome, _, _ in usuarios:  # Desempacotando nome e ignorando o resto
    print(nome, end='\t')