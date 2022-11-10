from abc import ABCMeta, abstractmethod
from operator import attrgetter  # Função para acesso de atributos


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

    def __eq__(self, other):  # Método para comparar a igualdade entre objetos, utilizando algum atributo.
        return self._codigo == other._codigo and self._saldo == other._saldo and type(self) == type(other)

    def __lt__(self, other):  # less then (menor que)
        if self._saldo != other._saldo:  # Caso os saldos sejam diferentes, compara o saldo
            return self._saldo < other._saldo
        return self._codigo < other._codigo  # Caso os saldos sejam iguais, compara o código


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

conta01 = ContaCorrente(101)
conta02 = ContaCorrente(101)
conta03 = ContaPoupanca(101)

print(conta01 == conta02)  # Comparação retorna true por causa do método __eq__
print(conta01 == conta03, '\n')

conta_guilherme = ContaCorrente(18)
conta_guilherme.depositar(500)

conta_daniela = ContaCorrente(19)
conta_daniela.depositar(1000)

conta_paulo = ContaCorrente(20)
conta_paulo.depositar(750)

contas = [conta_guilherme, conta_daniela, conta_paulo]

for conta in contas:
    print(conta)

print()

# Caso o método __lt__ não tenha sido implementado:
# Ordena os objetos através do atributo saldo, utilizando attrgetter
for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)

conta_guilherme.depositar(500)
conta_paulo.depositar(250)
print()

# Caso o método __lt__ não tenha sido implementado:
# Ordena os objetos através do atributo saldo, depois pelo código, utilizando attrgetter
for conta in sorted(contas, key=attrgetter('_saldo', '_codigo')):
    print(conta)

print()

# Comparando objetos (implementado na função __lt__):
print(conta_guilherme < conta_paulo)
