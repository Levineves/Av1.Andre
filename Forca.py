import os
import random

# Códigos de cores para o terminal
VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
MARROM   = "\033[38;5;130m"
PELE     = "\033[38;5;223m"
NEGRITO = "\033[1m"
FUNDO_DESTACADO = "\033[47;30;1m"
RESET = "\033[0m"

from palavrasecreta import palavra as lista_palavras

# Limpar tela do terminal usando o os.system
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Loop para manter o jogo rodando enquanto o jogador quiser continuar
while True:
    limpar_tela()

    # Escolhe a palavra e reseta as variáveis no início de CADA partida
    palavra = random.choice(lista_palavras)
    letras_jogador = []
    chances = 7
    ganhou = False

    # Desenhos simples do boneco da forca (estágio 0 ao estágio 7)
    boneco = [
        f"""
        {MARROM}   +---+
           |   |
               |
               |
              ==={RESET}""",
        f"""
        {MARROM}   +---+
           |   |
           {RESET}{PELE}O{RESET}{MARROM}   |
               |
              ==={RESET}""",
        f"""
        {MARROM}   +---+
           |   |
           {RESET}{PELE}O{RESET}{MARROM}   |
           {RESET}{PELE}|{RESET}{MARROM}   |
               |
              ==={RESET}""",
        f"""
        {MARROM}   +---+
           |   |
           {RESET}{PELE}O{RESET}{MARROM}   |
          {RESET}{PELE}/|{RESET}{MARROM}   |
               |
              ==={RESET}""",
        f"""
        {MARROM}   +---+
           |   |
           {RESET}{PELE}O{RESET}{MARROM}   |
          {RESET}{PELE}/|\\{RESET}{MARROM}  |
               |
              ==={RESET}""",
        f"""
        {MARROM}   +---+
           |   |
           {RESET}{PELE}O{RESET}{MARROM}   |
          {RESET}{PELE}/|\\{RESET}{MARROM}  |
          {RESET}{PELE}/{RESET}{MARROM}    |
              ==={RESET}""",
        f"""
        {MARROM}   +---+
           |   |
           {RESET}{PELE}O{RESET}{MARROM}   |
          {RESET}{PELE}/|\\{RESET}{MARROM}  |
          {RESET}{PELE}/ \\{RESET}{MARROM}  |
              ==={RESET}""",
        f"""
        {MARROM}   +---+
           |   |
           {RESET}{VERMELHO}X{RESET}{MARROM}   |
          {RESET}{VERMELHO}/|\\{RESET}{MARROM}  |
          {RESET}{VERMELHO}/ \\{RESET}{MARROM}  |
              ==={RESET}"""
    ]

    # LOOP INTERNO DA PARTIDA ATUAL
    while True:
        print("=== JOGO DA FORCA ===")
        print(boneco[7 - chances])
        print(f"{AMARELO}Letras que voce ja tentou: {letras_jogador}{RESET}")
        print("")

        # Lógica para exibir a palavra com traços ou letras descobertas
        for letra in palavra:
            if letra.lower() in letras_jogador:
                print(f"{FUNDO_DESTACADO} {letra.upper()} {RESET}", end=" ")
            else:
                print("_", end=" ")
        print("")
        print("")

        Tentativa = input("Digite uma letra: ")

        # Validações da tentativa
        if len(Tentativa) != 1 or not Tentativa.isalpha():
            print(f"{VERMELHO}Ops! Por favor, digite apenas UMA letra.{RESET}")
            print("-------------------------------")
            continue

        if Tentativa.lower() in letras_jogador:
            print(f"{VERMELHO}Você já tentou essa letra. Tente outra.{RESET}")
            print("-------------------------------")
            continue

        # Guarda a letra nova na lista
        letras_jogador.append(Tentativa.lower())

        if Tentativa.lower() not in palavra.lower():
            chances -= 1
            print(f"{VERMELHO}Você errou! Você ainda tem {chances} chances.{RESET}")
            print("-------------------------------")

        # Testa se o jogador acertou a palavra toda
        ganhou = True
        for letra in palavra:
            if letra.lower() not in letras_jogador:
                ganhou = False

        # Se perdeu todas as chances ou se ganhou, encerra a partida atual
        if chances == 0 or ganhou:
            break

    # Exibição do resultado do jogo
    print("")
    if ganhou:
        print(f"{VERDE}PARABÉNS, VOCÊ GANHOU! A PALAVRA ERA: {palavra}{RESET}")
    else:
        print(boneco[7])
        print(f"{VERMELHO}VOCÊ PERDEU! A PALAVRA ERA: {palavra}{RESET}")

    # Pergunta se quer jogar novamente
    print("")
    jogar_denovo = input("Deseja jogar novamente? (S/N): ").strip().upper()
    if jogar_denovo != "S":
        print("\nObrigado por jogar! Até a próxima.")
        break