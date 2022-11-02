# EXPRESSÕES REGULARES - REGULAR EXPRESSION -- RegEx
import re

endereco = 'Rua das Flores, 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'

# padrão cep -> 5 dígitos + hífen (opcional) + 3 dígitos:
# padrao_cep = re.compile('[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]')
# O símbolo '?' acima, implica que '-' pode aparecer 1 ou nenhuma vez

# Usando quantificadores:
padrao_cep = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')


busca = padrao_cep.search(endereco)  # Retorna Match ou None
if busca:
    cep = busca.group()  # Retorna a str encontrada no padrão criado
    print(cep)

# ---------------------------------

'''
Verifica se a base da URL está de acordo com o padrão correto.

Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URLs inválidas:
    https://bytebank/cambio
    https://bytebank.naoexiste/cambio
    ht://bytebank.naoexiste/cambio
'''

url = 'www.bytebank.com.br/cambio'

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError('A URL não é válida.')

print('A URL é válida.')