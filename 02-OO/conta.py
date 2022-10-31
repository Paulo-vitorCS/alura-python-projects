
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

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # Métodos Getters and Setters:
    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__titular

    def get_titular(self):
        return self.__titular

    def set_limite(self, limite):
        self.__limite = limite