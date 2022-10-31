
class Conta:
    # Definindo um construtor e passando os atributos como parâmetro:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    # Definindo os métodos da classe:
    def extrato(self):
        print('O saldo do titular {} é R$ {:.2f}'.format(self.titular, self.saldo))


    def depositar(self, valor):
        self.saldo += valor


    def sacar(self, valor):
        self.saldo -= valor


