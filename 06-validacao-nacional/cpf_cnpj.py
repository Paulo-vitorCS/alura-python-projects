# Pacotes utilizados:
#     pip install validate-docbr
from validate_docbr import CPF, CNPJ


class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento.lower()
        documento = str(documento)
        if self.tipo_documento == 'cpf':
            if self.valida_cpf(documento):
                self.cpf = documento
            else:
                raise ValueError('CPF inválido!')
        elif self.tipo_documento == 'cnpj':
            if self.valida_cnpj(documento):
                self.cnpj = documento
            else:
                raise ValueError('CNPJ inválido!')
        else:
            raise ValueError('Documento inválido.')

    @staticmethod
    def valida_cpf(cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError('Quantidade de digitos inválida.')

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.format_cpf()
        else:
            return self.format_cnpj()

    def valida_cnpj(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError('Quantidade de digitos inválida.')
