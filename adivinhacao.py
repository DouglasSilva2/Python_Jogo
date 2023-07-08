#criando uma função de adivinhacao!!!
def jogar():
    import random
    # importando a biblioteca randomica, para numeros aleatorios

    print('*' * 40)
    print('BEM VINDO AO PROGRAMA DE ADIVINHAÇÃO!')
    print('*' * 40)
    # variaveis do Jogo!!!
    # numero secreto que vai ser comparado para ver se é ou não
    numero_secreto = round(random.random() * 101)  # vai gerar um numero entre 0.0 e 1.0, até 100;
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('')
    print('Escolha o nivel do GAME: (1) Facil (2) Medio (3) Dificil')
    nivel = int(input('Digite o nivel que voce quer Jogar: '))

    # Estrutura de bloco para verificar se o valor digitado corresponde ao nivel de dificuldade!!

    # se nivel for  == a 1, executa uma parte; se nivel for == 2, executa outra parte; etc
    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 5
    elif (nivel == 3):
        total_de_tentativas = 2

    # loop para executar ate que o valor atenda o result do for
    for rodada in range(1, total_de_tentativas + 1):
        print('')
        print('Tentaivas {} de {}'.format(rodada, total_de_tentativas))
        chute = int(input('Digite o seu numero: '))
        print('Voce digitou: ', chute)
        # com o paramentro continue, vou retornar ao meu "for", para executrar noamente, pois o valor executado não alimenta a minha condição!
        if (chute < 1 or chute > 100):  # para  chute maior que 1 ou chute menor que 100, imprima ....
            print('Voce deve digiar um numero entre 1 e 100!')
            continue

        # comparação refente aos dados nas variaveis, chutou, e numero_secreto -- variavel do tipo " bool "
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print('Voce acertou e fez {} pontos!'.format(pontos))
            break  # finaliza o meu codigo, caso o valor seja verdadeiro..
        else:
            if (maior):
                print("Voce errou!! O Seu Chute foi maior do que o numero secreto!")
            elif (menor):
                print("Voce errou!! O Seu Chute foi menor do que o numero secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('')
    print('*' * 40)
    print(' FIM DO JOGO - VOCE FEZ {} PONTOS!!'.format(pontos))
    print('*' * 40)

if(__name__=="__main__"):
    jogar()