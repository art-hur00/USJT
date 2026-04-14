def buscaServidor(lista, alvo):
    for x in range(len(lista)):
        if lista[x] == alvo:
            return x
    return -1

print("Olá Bem vindo(a) ao programa verifica servidor")

entrada = input("Digite a lista de servidores(Separados apenas por espaço, sem vírgula!): ")
servidores = [int(item) for item in entrada.split()]

servidor_alvo = int(input("Digite o servidor que deseja verificar: "))
resultado = buscaServidor(servidores,servidor_alvo)

print(f"O servidor de ID{servidor_alvo} tem o indice {resultado}!")