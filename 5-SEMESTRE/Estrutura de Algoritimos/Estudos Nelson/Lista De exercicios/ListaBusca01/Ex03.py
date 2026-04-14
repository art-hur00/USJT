def buscalinear(lista, alvo):
    for x in range(len(lista)):
        if lista[x] == alvo:
            return x
    return -1

listaUsuario = input("Digite a lista de enderecos IP que tentaram acessar o sistema (A lista deve ser separada por espaços, sem virgula!)\n:")
lista = [int(item) for item in listaUsuario.split()]
alvo = int(input("Digite o IP que deseja verificar na lista: "))
resultado = buscalinear(lista, alvo)

if resultado != -1:
    print(f"O IP buscado está na lista! \n E tem o indice {resultado}")
else:
    print(f"O IP {alvo} nao está na lista!")
    
