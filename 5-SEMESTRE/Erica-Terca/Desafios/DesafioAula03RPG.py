#Arthur Alves Farias - RA: 824138792

class personagemPrincipal:
    def __init__(self, vida, poder, dano, resistencia):
        self.vida = vida
        self.poder = poder
        self.dano = dano
        self.resistencia = resistencia
        

class personagemVilao:
    def __init__(self, vidaV, poderV, danoV, resistenciaV):
        self.vidaV = vidaV
        self.poderV = poderV
        self.danoV = danoV
        self.resistenciaV = resistenciaV


vida = 2
poder = 2
dano = 2
resitencia = 2
pontosDisponiveis = 12


while pontosDisponiveis > 0:
    print("Selecione um atributo e quantos pontos deseja adicionar a ele: ")
  
    atributoSelecionado = int(input("Selecione o atributo que deseja adicionar: \n1-Vida \n2-Poder  \n3-Dano \n4-Resistência\n: "))
    pontosAtribuidos = int(input("Quantos pontos deseja adicionar?:"))

    if atributoSelecionado == 1:
        vida += pontosAtribuidos
        pontosDisponiveis -= pontosAtribuidos
        pontosAtribuidos = 0
        print("Vida: ", vida, "\nPontos ainda disponiveis: ", pontosDisponiveis)
    elif atributoSelecionado == 2:
        poder += pontosAtribuidos
        pontosDisponiveis -= pontosAtribuidos
        pontosAtribuidos = 0
        print("Poder Atual: ", poder, "\nPontos ainda disponiveis: ", pontosDisponiveis)
    elif atributoSelecionado == 3:
        dano += pontosAtribuidos
        pontosDisponiveis -= pontosAtribuidos
        pontosAtribuidos = 0
        print("Dano: ", dano, "\nPontos ainda disponiveis: ", pontosDisponiveis)
    elif atributoSelecionado == 4:
        resitencia += pontosAtribuidos
        pontosDisponiveis -= pontosAtribuidos
        pontosAtribuidos = 0
        print("Resistência: ", resitencia, "\nPontos ainda disponiveis: ", pontosDisponiveis)
    


