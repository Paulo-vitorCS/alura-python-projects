import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:
            return url.strip()  # Retira espaços em branco e caracteres especiais
        else:
            return ''  # Retorna string vazia

    def valida_url(self):
        if not self.url:  # Se a url for vazia, retorna falso e é negada,  resultando em erro:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é válida.')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)

        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + \
               'Parâmetros: ' + self.get_url_parametros() + '\n' + \
               'URL Base: ' + self.get_url_base()

    # Mudando o comportamento do __eq__, que inicialmente compara a igualdade entre os endereços de memória dos objetos
    def __eq__(self, other):
        return self.url == other.url


url_teste = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
extrator_url = ExtratorURL(url_teste)
extrator_url_2 = ExtratorURL(url_teste)

print('Tamanho da URL:', len(extrator_url))
print(extrator_url, '\n')

print(extrator_url == extrator_url_2)
print(id(extrator_url))
print(id(extrator_url_2))

valor_quantidade = extrator_url.get_valor_parametro('Origem')
print('\n', valor_quantidade)
