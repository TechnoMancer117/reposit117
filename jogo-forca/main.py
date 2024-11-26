import random

def jogar_forca():
    palavras = ['python', 'programacao', 'algoritmo', 'computador']
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ['_' for _ in palavra_secreta]
    tentativas = 6

    while tentativas > 0 and '_' in letras_descobertas:
        print(" ".join(letras_descobertas))
        letra = input("Digite uma letra: ").lower()

        if letra in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_descobertas[i] = letra
        else:
            tentativas -= 1
            print(f"Errou! Você tem {tentativas} tentativas restantes.")

    if '_' not in letras_descobertas:
        print(f"Parabéns! Você acertou: {palavra_secreta}")
    else:
        print(f"Fim de jogo! A palavra era: {palavra_secreta}")

# Inicia o jogo
jogar_forca()