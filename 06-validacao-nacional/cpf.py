# Pacotes utilizados:
#     pip install validate-docbr
from validate_docbr import CPF


class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!')

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

    def __str__(self):
        return self.format_cpf()
