from cpf_cnpj import Documento
from telefoneBr import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

cpf = '32007832062'
exemplo_cpf = Documento.criar_documento(cpf)
print(exemplo_cpf)

cnpj = '35379838000112'
exemplo_cnpj = Documento.criar_documento(cnpj)
print(exemplo_cnpj, '\n')
# ------------------------------------------------------

telefone = '552126451234'
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto, '\n')
# ------------------------------------------------------

cadastro = DatasBr()
print(cadastro.tempo_cadastro(), '\n')
# ------------------------------------------------------

cep = '01001000'
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)