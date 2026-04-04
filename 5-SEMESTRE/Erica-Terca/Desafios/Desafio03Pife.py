#Arthur Alves farias
from random import shuffle

#espada = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141]
#copas = [12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142]
#ouros = [13, 23, 33, 43, 53, 63, 73, 83, 93, 103, 113, 123, 133, 143]
#paus = [14, 24, 34, 44, 54, 64, 74, 84, 94, 104, 114, 124, 134, 144]

#Cartas e embaralhamento
cartas = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142, 13, 23, 33, 43, 53, 63, 73, 83, 93, 103, 113, 123, 133, 143, 14, 24, 34, 44, 54, 64, 74, 84, 94, 104, 114, 124, 134, 144]
shuffle(cartas)


#Separação da mão

cartasJogador = []
cartasJogador.extend(cartas[:9])
del cartas[:9]
shuffle(cartas)

cartasAdversario = []
cartasAdversario.extend(cartas[:9])
del cartas[:9]
shuffle(cartas)

cartaNaMesa = []
cartaNaMesa.extend(cartas[:1])
del cartas[:9]

print(cartasAdversario)
print(cartasJogador)
print(cartaNaMesa)
print(cartas)