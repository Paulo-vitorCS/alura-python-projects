url = 'bytebank.com/cambio?moedaOrigem=real'

url_base = url[0:19]
print(url_base)

url_parametros = url[20:36]
print(url_parametros, '\n')

# -------------------------------------------------------------------- #

url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'

# TRATAMENTO DE EXCEÇÕES:
# Sanitização da URL:
#url = url.replace(' ', '')  # Substituindo espaços em branco por uma str vazia, ou
url = url.strip()

# Validação da URL:
if url == '':
    raise ValueError('A URL está vazia.')

# SEPARANDO A BASE E OS PARAMETROS:
indice_interrogacao = url.find('?')

# O python identifica o inicio da string quando omitido o valor
url_base = url[:indice_interrogacao]
print(url_base)

# De forma análoga, identifica o fim omitindo o valor:
url_parametros = url[indice_interrogacao+1:]
print(url_parametros, '\n')

# BUSCANDO O VALOR DE UM PARAMETRO:
# parametro_busca = 'moedaOrigem'
# parametro_busca = 'moedaDestino'
parametro_busca = 'quantidade'

indice_parametro = url_parametros.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
