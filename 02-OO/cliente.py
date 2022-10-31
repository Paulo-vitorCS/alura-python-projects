
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    # O acesso ao método não necessita dos parenteses (), como se acessassemos diretamente o atributo;
    # Para isso usa-se @property (Método getter sem o get):
    @property
    def nome(self):
        print('Chamando @property nome()')
        return self.__nome.title()

    # De forma análoga, criando um setter sem o set
    @nome.setter
    def nome(self, nome):
        print('Chamando o setter nome()')
        self.__nome = nome