

palavra = "python"

letras_jogador = []
chances = 7
ganhou = False

while True:
    #criando a logica
    for letra in palavra:
        if letra.lower() in letras_jogador:
            print(letra, end = " ")

        else:
            print("_", end = " ")
    print("")
    print("")

    Tentativa = input("Digite uma letra: ")
    letras_jogador.append(Tentativa.lower())
    if Tentativa.lower() not in palavra.lower():
        chances -= 1
        print(f"Você errou! Você ainda tem {chances} chances.")

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_jogador:
            ganhou = False
            

    if chances == 0 or ganhou:
        break


if ganhou:
    print(f"PARABÉNS, VOCE GANHOU! A PALAVRA ERA: {palavra}")
else:
    print(f"VOCÊ PERDEU! A PALAVRA ERA: {palavra}")