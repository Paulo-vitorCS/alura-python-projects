from cpf_cnpj import CpfCnpj

cpf = '32007832062'
objeto_cpf = CpfCnpj(cpf, 'cpf')
print(objeto_cpf)

cnpj = '35379838000112'
objeto_cnpj = CpfCnpj(cnpj, 'cnpj')
print(objeto_cnpj)