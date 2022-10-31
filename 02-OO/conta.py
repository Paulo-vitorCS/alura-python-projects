
class Conta:
    # Definindo um construtor e passando os atributos como parâmetro:
    def __init__(self, numero, titular, saldo, limite):
        # Atributo com __ é privado (private):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Definindo os métodos da classe:
    def extrato(self):
        print('O saldo do titular {} é R$ {:.2f}'.format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('O valor {} ultrapassa o limite.'.format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # Métodos Getters and Setters:
    def get_saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def get_titular(self):
        return self.__titular

    # Método estático, pertencente a classe (não precisa criar um objeto para acessa-lo)
    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa' : '104', 'Bradesco' : '237'}
