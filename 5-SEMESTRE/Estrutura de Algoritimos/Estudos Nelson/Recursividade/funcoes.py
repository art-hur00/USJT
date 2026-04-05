#Ex1:Receba um numero e imprima a sequencia deste numero até zero.
#def Regressivo(num):
#    print(num)
#    if num == 0:
#        return 0
#    return Regressivo(num - 1)
#Regressivo(10)
#Ex2:Receve uma lista e retorne o maior numero dessa lista
#def maiorNumero(*lista):
#    if len(lista) == 1:
#        return lista[0]
#    atual = lista[0]
#    while len(lista) > 1:
#        if atual < lista[1]:
#           return maiorNumero(*lista[1:]) 
#        else:
#           nova_lista = (atual,) + lista[2:]
#           return maiorNumero(*nova_lista)
# 
#resultado = maiorNumero(12, 3 , 4 ,32 , 18, 2)
#print(resultado)

#def soma(a, b):
#    resultado = a + b
#    return resultado
#conta = soma(5, 5)
#print(conta)