from cpf_cnpj import Documento
from telefoneBr import TelefonesBr

cpf = '32007832062'
exemplo_cpf = Documento.criar_documento(cpf)
print(exemplo_cpf)

cnpj = '35379838000112'
exemplo_cnpj = Documento.criar_documento(cnpj)
print(exemplo_cnpj, '\n')
# ------------------------------------------------------

telefone = '552126451234'
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)
