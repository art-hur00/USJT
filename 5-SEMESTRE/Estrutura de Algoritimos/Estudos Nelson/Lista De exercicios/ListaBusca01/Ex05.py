def buscaLista(lista, alvo):
    for x in range(len(lista)):
        if lista[x] == alvo:
            return x
    return -1

print("Bem vindo ao Busca acoes!")

entrada = input("Digite a lista de acoes: ").replace(',', ' ')
lista_acoes = entrada.split()

resultado = buscaLista(lista_acoes, "MGLU3")

if resultado != -1:
    print(f"A acao MGLU3 está na lista! (Encontrada no índice {resultado})")
else:
    print("A acao MGLU3 nao está na lista!")