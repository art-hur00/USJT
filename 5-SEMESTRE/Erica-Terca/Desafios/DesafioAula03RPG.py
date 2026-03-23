# Arthur Alves Farias - RA: 824138792

import random
#Classe heroi
class personagemPrincipal:
    def __init__(self, vida, forca, resistencia):
        self.vida = vida
        self.forca = forca
        self.resistencia = resistencia

vida = 2
forca = 5
poder = (vida + forca) / 2
resitencia = 2
pontosDisponiveis = 12

#Classe Vilão
class personagemVilao:
    def __init__(self, vidaI1, forcaI1, danoI1, resistenciaI1):
        self.vidaI1 = vidaI1
        self.forcaI1 = forcaI1
        self.danoI1 = danoI1
        self.resistenciaI1 = resistenciaI1

#Atributos Inimigo1
vidaI1 = 10
forcaI1 = 2
resistenciaI1 = 5
poderI1 = (vidaI1 + forcaI1) /2

#Seleção de atributos
while pontosDisponiveis > 0:

    print("Selecione um atributo e quantos pontos deseja adicionar a ele, ")

    atributoSelecionado =  (int(input("Selecione o atributo que deseja adicionar: \n1-Vida \n2-Força  \n3-Resistência\n: ")))
    pontosAtribuidos = int(input("Quantos pontos deseja adicionar?:"))

    if atributoSelecionado == 1:
        vida += pontosAtribuidos
        pontosDisponiveis -= pontosAtribuidos
        pontosAtribuidos = 0
        print("Vida: ", vida, "\nPontos ainda disponiveis: ", pontosDisponiveis)
    elif atributoSelecionado == 2:
        forca += pontosAtribuidos
        pontosDisponiveis -= pontosAtribuidos
        pontosAtribuidos = 0
        print("Força Atual: ", forca, "\nPontos ainda disponiveis: ", pontosDisponiveis)
    elif atributoSelecionado == 3:
        resitencia += pontosAtribuidos
        pontosDisponiveis -= pontosAtribuidos
        pontosAtribuidos = 0
        print("Resistência: ", resitencia, "\nPontos ainda disponiveis: ", pontosDisponiveis)


#Sistema de ataque
dano = forca - resistenciaI1
danoV = forcaI1 - resitencia

#Primeira Ação do jogo

while vidaI1 > 0  :
   acao1 = (int(input("Você se deparou com um inimigo, o que deseja fazer: \n1-Atacar\n2-Fugir")))

   if  acao1 == 1:
    vidaI1 -= dano
    print("Dano ao inimigo: ", dano, "\nVida inimigo: ", vidaI1)

   elif acao1 == 2:
       if poder > poderI1:
            print("Fugiu")
            vidaI1 = 0
       elif poder < poderI1:
           vida -= danoV
           print("Dano inimigo: ", danoV)
           print("Vida restante: ", vida)


print("Voce se deparou com um báu, deseja abri-ló? ")
acao2 = (int(input("1-Sim\n2-Não")))

if acao2 == 1:
    dano += 5
    print("Você recebeu uma espada nova!\nDano + 5\nDano total: ", dano)
    print("Você recebeu uma poção de cura!\nCura 5 de hp")
elif acao2 == 2:
    poder += 10
    print("Sua braveza e honestidade te enchem de poder\nPoder= + 10\nPoder total: ", poder)


