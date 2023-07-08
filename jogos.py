#importando os meus arquivos de jogos!!!

import forca
import adivinhacao

#cabeçalho do meu jogo
print('*'*39)
print('**** ESCOLHA O SEU JOGO ****')
print('*'*39)

print(' (1) FORCA (2) ADIVINHAÇÃO')
print('________________________________________')
print('-- QUAL JOGO VOCE QUER JOGAR ?')
jogo = int(input('N:.:'))


#condição de escolha do meu jogo!!
if(jogo == 1):
    print('Jogando forca')
    forca.jogar()
elif(jogo == 2):
    print('Jogando adivinhação')
    adivinhacao.jogar()