def jogar():
    print("*********************************")
    print("*  Bem vindo ao jogo da Forca!  *")
    print("*********************************")

    palavra_secreta = "banana".lower()
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

        enforcou = erros == len(palavra_secreta)
        acertou = '_' not in letras_acertadas

    if acertou:
        print('\n*** Você ganhou! ***')
    else:
        print('\n*** Você perdeu! ***')
    print("\nFim do jogo")


# Caso queira rodar diretamente forca.py
if __name__ == "__main__":
    jogar()
