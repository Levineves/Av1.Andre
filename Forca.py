import  random

# Códigos de cores para o terminal
VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
MARROM   = "\033[38;5;130m"
PELE     = "\033[38;5;223m"
NEGRITO = "\033[1m"
FUNDO_DESTACADO = "\033[47;30;1m"
RESET = "\033[0m"

from palavrasecreta import palavra
#List com algumas palavras para o jogo escolher uma de forma aleatoria do palavrasecreta.py
palavra = random.choice(palavra)

letras_jogador = []
chances = 7
ganhou = False

# Desenhos simples do boneco da forca (do estagio 0 ao estagio 7)
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
      {RESET}{PELE}/|\{RESET}{MARROM}  |
           |
          ==={RESET}""",
    f"""
    {MARROM}   +---+
       |   |
       {RESET}{PELE}O{RESET}{MARROM}   |
      {RESET}{PELE}/|\{RESET}{MARROM}  |
      {RESET}{PELE}/{RESET}{MARROM}    |
          ==={RESET}""",
    f"""
    {MARROM}   +---+
       |   |
       {RESET}{PELE}O{RESET}{MARROM}   |
      {RESET}{PELE}/|\{RESET}{MARROM}  |
      {RESET}{PELE}/ \{RESET}{MARROM}  |
          ==={RESET}""",
    f"""
    {MARROM}   +---+
       |   |
       {RESET}{VERMELHO}X{RESET}{MARROM}   |
      {RESET}{VERMELHO}/|\{RESET}{MARROM}  |
      {RESET}{VERMELHO}/ \{RESET}{MARROM}  |
          ==={RESET}"""
]

print("=== JOGO DA FORCA ===")

while True:
    
    #1. Mostrar o boneco da forca de acordo com as chances restantes
    # Mostrar as letras que o jogador já acertou e as letras que ainda não foram acertadas
    print(boneco[7 - chances])
    print(f"{AMARELO}Letras que voce ja tentou: {letras_jogador}{RESET}")
    print("")

    #criando a logica
    for letra in palavra:
        if letra.lower() in letras_jogador:
            print(f"{FUNDO_DESTACADO} {letra.upper()} {RESET}", end=" ")

        else:
            print("_", end = " ")
    print("")
    print("")

    Tentativa = input("Digite uma letra: ")
    #3. Verifica se o usuario digitou algo invalido ou uma letra repetida
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
            

    if chances == 0 or ganhou:
        break

# Fim de jogo
print("")
if ganhou:
    print(f"{VERDE}PARABÉNS, VOCE GANHOU! A PALAVRA ERA: {palavra}{RESET}")
else:
    print(boneco[7 - chances])
    print(f"{VERMELHO}VOCÊ PERDEU! A PALAVRA ERA: {palavra}{RESET}")