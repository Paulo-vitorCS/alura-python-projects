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