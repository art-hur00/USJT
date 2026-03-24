# Arthur Alves Farias - RA: 824138792

import random



#Classe heroi
class personagemPrincipal:
    def __init__(self, vida, forca, resistencia):
        self.vida = vida
        self.forca = forca
        self.resistencia = resistencia

vida = 3
forca = 5
poder = (vida + forca) / 2
resistencia = 5
pontosDisponiveis = 12
#-------------------------------
#Classe Vilão
class personagemInimigo1:
    def __init__(self, vidaI1, forcaI1, danoI1):
        self.vidaI1 = vidaI1
        self.forcaI1 = forcaI1
        self.danoI1 = danoI1

class personagemInimigo2:
    def __init__(self, vidaI2, forcaI2, danoI2):
        self.vidaI2 = vidaI2
        self.forcaI2 = forcaI2
        self.danoI2 = danoI2

class personagemBoss:
    def __init__(self, vidaC, forcaC, danoC):
        self.vidaC = vidaC
        self.forcaC = forcaC
        self.danoC = danoC

#Atributos Inimigo1
vidaI1 = 5
forcaI1 = 2
poderI1 = (vidaI1 + forcaI1) /2

#Atributos Inimigo2
vidaI2 = 14
forcaI2 = 4
poderI2 = (vidaI2 + forcaI2) /2

#Atributos Chefao
vidaC = 24
forcaC = 8


#Comeco do jogo
nomePersonagem = input("Qual o seu nome?: ")
nomeVilao = input("Qual o nome do seu grande inimigo?: ")
tesouro = input("O que "+ nomeVilao + " roubou de você?: ")

print("\nAh sim, já ouvi falar de você, realmente o que", nomeVilao,"fez foi horrível!")

print("Se retomar seu", tesouro, "é o que deseja, sei onde ele vive. Siga aquela floresta densa e escura até encontrar um castelo voador, ali é onde", nomeVilao, "se esconde.")

print("\nMas antes de ir, preciso saber ser é pareo para o desafio.")

print("Bem vindo a criação de personagem, aqui você poderá montar os atributos de seu personagem")

print("Atributos base: \nVida:", vida, "\nForça:", forca, "\nResistência:", resistencia)

print("Você tem 12 pontos para distribuir como desejar.")

print("Cada atributo tem sua importância, então escolha sabiamente...\n")


#Seleção de atributos
while pontosDisponiveis > 0:

    atributoSelecionado =  (int(input("Selecione o atributo que deseja adicionar: \n1-Vida \n2-Força  \n3-Resistência\n: ")))
    pontosAtribuidos = int(input("Quantos pontos deseja adicionar?\n:"))

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
        resistencia += pontosAtribuidos
        pontosDisponiveis -= pontosAtribuidos
        pontosAtribuidos = 0
        print("Resistência: ", resistencia, "\nPontos ainda disponiveis: ", pontosDisponiveis)


#Sistema de ataque
danoI1 = forcaI1 - (resistencia/2)
danoI2 = forcaI2 - (resistencia/2)
danoC = forcaC - (resistencia/2)

#Confronto com lobo
print("\nCaminhando pela floresta voce se depara com um feroz lobo")
while vidaI1 > 0 and vida > 0 :
   print("\n\nEstatos do lobo: \nVida:", vidaI1, "\nForça: ", forcaI1,)
   acao1 = (int(input("O que deseja fazer: \n1-Atacar\n2-Fugir\n: ")))

   if  acao1 == 1:
       dano = forca - (random.randrange(10) / 10)
       vidaI1 -= dano
       print("Você o ataca!")
       print("Dano:", dano, "Vida restante:", vidaI1)
       if vidaI1 > 0:
        print("\nLobo te ataca")
        vida -= danoI1
        print("Dano", danoI1, "Vida restante:", vida)

   elif acao1 == 2:
       if poder > poderI1:
            print("Fugiu")
            vidaI1 = 0
       elif poder < poderI1:
           vida -= danoI1
           print("O lobo te impede de fugir!\nE te ataca!")
           print("Dano inimigo: ", danoI1)
           print("Vida restante: ", vida)

if vida < 0:
    print("Lobo te devora")
    print("Voce morreu!\n")
elif vidaI1 < 0:
    print("Parabéns, você o derrotou\nMas aquele pobre lobo nunca foi um verdadeiro adversário")


#Báu
print("Seguindo seu caminho pela densa floresta voce se depara com um báu, deseja abri-ló?\n: ")
acao2 = (int(input("1-Sim\n2-Não")))

if acao2 == 1:
    dano += 5
    vida += 5
    print("Você recebeu uma espada nova!\nDano + 5\nDano total: ", dano)
    print("Você recebeu uma poção de cura!\nVida  + 5\nVida total: ", vida)

elif acao2 == 2:
    poder += 10
    print("Sua braveza e honestidade te enchem de poder\nPoder= + 10\nPoder total: ", poder)



#Sala do enigma
print("\nVocê finalmente sai da floresta, a sua frente está o temido castelo, seus muros parecem não tem fim.\nVê uma pequena entrada no meio do castelo e decide entrar")
print("Entrando na porta se depara com um calabouso não há nada lá além de uma frase gravada na parede e um livro em branco. Você se depara com um enigma!\nA porta de onde você saiu não existe mais.")
print("\nEu falo sem ter uma boca, eu escuto sem ter ouvidos. Eu não tenho um corpo, mas me torno vivo com o vento. O que sou eu?")
respostaEnigma = input("\nResposta para o enigma: ")

if respostaEnigma == "eco":
    print("\nA parede onde o enigma estava escrito se abre a sua frente. Lá há um corredor estreito, porém longo, no final dele você vê", nomeVilao, "ele está sentado. Quieto. Apenas te observando")
else:
    print("\nFlechas se atiram em sua direção")
    print("\nElas te atigem em cheio...")
    print("Você sente a fria presença da morte, sua hora chegou.\n\n\n\n")
    print("Porém! Dentro daquele horrível castelo com paredes que parecem sem fim você ouve seu nome", nomePersonagem, nomePersonagem, "é ", tesouro, "você se enche de determinação e segue em sua jornada")
    print("Você teve vários ferimentos. \nVida = 1\nPorém se sente mais forte do que nunca!\nForça + 10")
    vida = 1
    forca += 10
print("Ao passar pelo meio do corredor algo pula em sua direção, parece um borrão e é. Sua figura é extremamente díficl de decifrar, mas algo é certo te matar seria uma grande demostração de força para", nomeVilao)


#Confronto com monstro
while vidaI2 > 0 and vida > 0 :
   print("\n\nEstatos do ???: \nVida:", vidaI2, "\nForça: ", forcaI2)
   acao3 = (int(input("O que deseja fazer: \n1-Atacar\n2-Fugir \n:")))

   if  acao3 == 1:
    dano = forca - (random.randrange(10) / 10)
    vidaI2 -= dano
    print("Você o ataca!")
    print("Dano:", dano, "Vida restante:", vidaI2)
    if vidaI2 > 0:
        print("\n??? te ataca")
        vida -= danoI2
        print("Dano", danoI2, "Vida restante:", vida)

   elif acao3 == 2:
       if poder > poderI2:
            print("Fugiu")
            vidaI2 = 0
       elif poder < poderI2:
           vida -= danoI2
           print("Dano inimigo: ", danoI2)
           print("Vida restante: ", vida)

if vidaI2 < 0:
    print("Parabéns, você derrotou aquilo!\nSeu grande confronto está perto.")
    forca += 2
    vida += 2
elif vida > 0:
    print("Após uma intensa luta aquela coisa arranca sua cabeça de forma impiedosa.\nVocê morreu!")

print("Continuando a caminho de seu objetivo final você encontra ele", nomeVilao, " se divertindo com seu", tesouro)


#Confronto BOSS
while vidaC > 0 and vida > 0 :
   print("\n\nEstatos do",nomeVilao, "\nVida:", vidaC, "\nForça: ", forcaC)
   acao3 = (int(input("O que deseja fazer: \n1-Atacar\n2-Fugir ")))

   if  acao3 == 1:
    dano = forca - (random.randrange(10) / 10)
    vidaC -= dano
    print("Você o ataca!")
    print("Dano:",dano,"Vida restante:",vidaC )
    if vidaC > 0:
        print("\n",nomeVilao, "te ataca")
        vida -= danoC
        print("Dano", danoC,"Vida restante:", vida)
   elif acao3 == 2:
       print("Não há escapatória")

if vida < 0 and vidaC < 0:
     print("Ambos morreram.")
elif vida < 0:
    print("Voce morreu!\n")
elif vidaC < 0:
    print("Parabéns, você o derrotou\n")
    print("E saiu daquele lugar horrível junto com seu", tesouro)
print("Fim")
print("Obrigado por jogar!")
