import random


def jogar():
    print("*********************************")
    print("*  Bem vindo ao jogo da Forca!  *")
    print("*********************************")

    arquivo = open('palavras.txt', 'r')

    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].lower()
    letras_acertadas = ['_'] * len(palavra_secreta)
    erros = 0

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("\nQual letra? ").strip().lower()

        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] = chute
                posicao += 1
        else:
            erros += 1

        print(letras_acertadas)

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

    if acertou:
        print('\n*** Você ganhou! ***')
    else:
        print('\n*** Você perdeu! ***')
    print("\nFim do jogo")


# Caso queira rodar diretamente forca.py
if __name__ == "__main__":
    jogar()
