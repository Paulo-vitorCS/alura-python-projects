from bytebank import Funcionario


class TestClass:
    # Para que o python reconheça como test, primeiramente se escreve test_ nos métodos e arquivos
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):  # Given-when-then (metodologia)
        # Given - Contexto
        entrada = '13/03/2000'
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When - Ação

        assert resultado == esperado  # Then - Desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho'  # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()  # When

        assert resultado == esperado # Then