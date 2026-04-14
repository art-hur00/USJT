def ordenacao(lista):
    for x in range(len(lista)):
        menor_indice = x
        for y in range(x + 1, len(lista)):
           if lista[y] < lista[menor_indice]:
             menor_indice = y
        lista[x], lista[menor_indice] = lista[menor_indice], lista[x]
    return lista

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] > alvo:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1

print("Bem vindo ao Verificador de Preços !")

entrada = input("Digite sua lista de preços\nLembrando que os preços devem estar separados espaço e nao virgula!\n:")
lista = [int(item) for item in entrada.split()]
listaOrdenada = ordenacao(lista)

alvo = int(input("Digite o preço que deseja verificar se está na lista: "))

resultado = busca_binaria(listaOrdenada, alvo)

if resultado != -1:
    print(f"O preço {alvo} está na lista, com indice: {resultado}")
else:
    print(f"O preço {alvo} nao está na lista")