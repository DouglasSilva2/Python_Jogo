import random
def jogar():
    #função de mensagem de abertura!!
    imprime_mensagem_abertura()
    palavra_secreta = carre_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)  # inicializando minha lista... para cada letra secreta -  list compregensions
    print(letras_acertadas)

    # inicialização da minha variavel ...
    enforcou = False
    acertou = False
    erros = 0

    # inicio do loop para o GAME!!! Executa ate que seja verdareiro a condição!!!
    # enquanto não se enforcou e não acertou, execute o loop!!!!
    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:  # chute está dentro da palavra secreta ? Se sim, execute !!
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        else:  # se não estiver, execute !!!
            # erros = erros + 1  ----- posso fazer o incremento assim, ou assim.. erros += 1
            erros += 1 #mais um erro para o usuario!!!
            desenha_forca(erros)

            enforcou = erros == 7  # vou verificar se o valor da variavel deu como erro, no caso a variable
            # enforcouse, pois ela já inicia como verdadeira
            # se for, ele vai incrementar o valor, e permitir uma nova jogada!!!
            acertou = '_' not in letras_acertadas  # enquato não tiver o '_' dentro das letras acertadas..
            print(letras_acertadas)
    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

# funçoes utilizadas nos Jogo!!
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#Função para imprimir mensagem de bem vindo na tela!
def imprime_mensagem_abertura():
    print('*****************************************')
    print('**** BEM VINDO AO JOGO DE FORCA ****')
    print('*****************************************')

def carre_palavra_secreta():
    arquivo = open("palavras.txt", "r")  # Abrindo meu arquivo pa
    palavras = []
    # Leitura do meu arquivo palavras, onde está contigo todas as informações do meu arquivo
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    # fim da inicialização da minha palavra secreta !!!
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
def inicializa_letras_acertadas(palavra):
    lista = ["_" for letra in palavra]
    return lista
def pede_chute():
    chute = input('Qual a letra vai chutar? ::..  ')
    chute = chute.strip().upper()
    return chute
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0  # quero saber a possição da minha letra, no meu GAME
    # para letra em palavra secreta, verifica se possui..
    for letra in palavra_secreta:
        if chute == letra:  # upper vai comparar mesmo sendo letra maiusculas, ou minusculas
            letras_acertadas[index] = letra  # vou amarzenar em letras acertadas o conteudo da minha lista!!
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
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
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    jogar()