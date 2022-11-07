from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):  # Definindo a classe como abstrata
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    @abstractmethod
    def taxa_conta(self):
        pass

    def __str__(self):
        return '[Código: {} | Saldo: R$ {:.2f}]'.format(self._codigo, self._saldo)


class ContaCorrente(Conta):
    def taxa_conta(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def taxa_conta(self):
        self._saldo *= 1.01
        self._saldo -= 3


conta = ContaCorrente(15)
conta.depositar(500)
print(conta)

conta2 = ContaCorrente(4500)
conta2.depositar(1000)
print(conta2)

contas = [conta, conta2]
print(contas)

conta16 = ContaCorrente(16)
conta16.depositar(1000)
conta16.taxa_conta()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.depositar(1000)
conta17.taxa_conta()
print(conta17)

contas = [conta16, conta17]

for conta in contas:
    conta.taxa_conta()
    print(conta)