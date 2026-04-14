def buscaNotas(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] > alvo:
            fim = meio -1
        else:
            inicio = meio + 1
    return -1
        
def ordenacao(lista):
    for x in range(len(lista)):
        menor_indice = x
        for y in range(x + 1, len(lista)):
            if lista[y] < lista[menor_indice]:
                menor_indice = y
        lista[x], lista[menor_indice] = lista[menor_indice], lista[x]
    return lista

print("Ola bem vindo ao verifica notas!")

notasUsuario = input("Digite a lista de notas(Separadas por espaço! Sem virgula!) :")
notas = [int(item) for item in notasUsuario.split()]
notasOrdenadas = ordenacao(notas)

alvo = int(input("Digite o alvo: "))

resultado = buscaNotas(notasOrdenadas, alvo)
if resultado != -1:
    print(f"A nota{alvo} esta na lista! ")
else:
    print(f"A nota{alvo} nao esta na lista!")