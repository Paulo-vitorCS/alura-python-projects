def jogar():
    print("*********************************")
    print("*  Bem vindo ao jogo da Forca!  *")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ['_'] * len(palavra_secreta)

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        print(letras_acertadas)

        chute = input("\nQual letra: ").strip()

        posicao = 0
        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                letras_acertadas[posicao] = chute
            posicao += 1

    print("Fim do jogo")


# Caso queira rodar diretamente forca.py
if __name__ == "__main__":
    jogar()

