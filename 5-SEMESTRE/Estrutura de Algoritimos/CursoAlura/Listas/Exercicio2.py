#atletas = [
#    ["Leorardo do Amaral Quinquio", 1.70, 53],
#    ["Yuri alberto", 1.82, 75],
#    ["Flavio Cacarrato", 2.23, 51],
#    ["Ferreira", 1.73, 21],
#    ["Wellington Mouse",1.72, 77 ],
#    ["Lucas Ribamar Lopes dos Santos Bibiano", 1.84, 79],
#    ["Barack Hussein Obama II", 1.74, 59]
#]
#listConversao = []
#for atleta in atletas:
#atletasTupla = tuple(listConversao)
# #
#print(atletasTupla)

#----------#----------#----------#----------#----------

#Lista
atletas = [
    ["Rogério Ceni", 1.88, 73],
    ["Rebeca Rodrigues de Andrade", 1.51, 56],
    ["Usain St. Leo Bolt", 1.95, 53],
    ["Michael Fred Phelps II", 1.93, 67],
    ["Simone Arianne Biles", 1.42, 52],
    ["Isaquias Queiroz dos Santos", 1.75, 62],
    ["Gabriel Medina Pinto Ferreira", 1.80, 79],
    ["Rayssa Leal", 1.60, 48],
    ["Marta Vieira da Silva", 1.62, 50],
    ["Robert Scheidt", 1.88, 73],
    ["Serena Jameka Williams", 1.75, 54],
    ["Arthur Nabarrete Zanetti", 1.56, 76],
    ["Alison dos Santos (Piu)", 1.98, 55],
    ["Mayra Aguiar da Silva", 1.78, 74],
    ["Thiago Braz da Silva", 1.83, 82],
    ["Eliud Kipchoge", 1.67, 71],
    ["Caio de Almeida Bonfim", 1.74, 74],
    ["Beatriz de Souza", 1.78, 57],
    ["Ana Marcela de Jesus Soares da Cunha", 1.66, 64],
    ["Gabriel Barbosa Almeida (Gabigol)", 1.76, 69]
]

#Declaração da lista tupla para conversão: lista -> tupla
atletas_tuplas = []

#Conversão lista -> Tupla
for atleta in atletas:
    nome = atleta[0]
    altura = atleta[1]
    peso = atleta[2]
    conversao_lista_tupla =  (nome, altura, peso)
    #---
    atletas_tuplas.append(conversao_lista_tupla)

#Declaraç]ao variável para calculo de média
numero_Atletas = 0

#Impressão da lista ordenada no console.

for nome, altura, peso in atletas_tuplas:
    print(f"\nFicha de: {nome}\nPeso: {peso}Kg \nAltura: {altura}m\n")
    numero_Atletas += 1

#Declaração das variáveis do cálculo de médias. 
peso_geral = sum([peso[2] for peso in atletas_tuplas])
media_de_peso = (peso_geral / numero_Atletas )
                                                
altura_geral = sum([altura[1] for altura in atletas_tuplas])
media_de_altura = (altura_geral / numero_Atletas)

#Impressão no console das médias
print(f"Peso total dos atletas: {peso_geral}kg\nPeso médio dos atletas: {media_de_peso}\nkg")

print(f"Altura total dos atletas: {altura_geral}m\nAltura média dos atletas: {media_de_altura:.2f}m\n")