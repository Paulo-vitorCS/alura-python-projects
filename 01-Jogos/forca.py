import random


def jogar():
    print("*********************************")
    print("*  Bem vindo ao jogo da Forca!  *")
    print("*********************************")

    palavra_secreta, letras_acertadas = sorteia_palavra_secreta()

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
            desenha_forca(erros)

        print(letras_acertadas)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("\nFim do jogo")


def sorteia_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()
    letras_acertadas = ['_'] * len(palavra_secreta)

    return palavra_secreta, letras_acertadas


def imprime_mensagem_vencedor():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________    ")
    print("   /               \   ")
    print("  /                 \  ")
    print(" /                   \ ")
    print(" |   XXXX     XXXX   | ")
    print(" |   XXXX     XXXX   | ")
    print(" |   XXX       XXX   | ")
    print(" |                   | ")
    print(" \__      XXX      __/ ")
    print("   |\     XXX     /|   ")
    print("   | |           | |   ")
    print("   | I I I I I I I |   ")
    print("   |  I I I I I I  |   ")
    print("   \_             _/   ")
    print("     \_         _/     ")
    print("       \_______/       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if  erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


# Caso queira rodar diretamente forca.py
if __name__ == "__main__":
    jogar()
