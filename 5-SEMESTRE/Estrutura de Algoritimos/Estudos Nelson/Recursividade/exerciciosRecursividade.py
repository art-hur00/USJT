#def funcao_recursiva(parametro):
    # 1. CASO BASE (A saída de emergência)
#    if parametro == 0: 
#        return 0
    
    # 2. PASSO RECURSIVO (Onde a mágica acontece)
 #   else:
  #      return parametro + funcao_recursiva(parametro - 1)


#Ex1:
#def contagemRegressiva(num):
#    if num < 0:
#        return
#    print(num)
#    contagemRegressiva(num - 1)

#valor = contagemRegressiva(5) 

#Ex2:
#def somaNaturais(num):
#    if num == 0:
#        return 0
#    return num + somaNaturais(num - 1)

#resultado = somaNaturais(2)
#print(resultado)

#Ex3:
#def calculaPotencia(base, expoente):
#    if expoente == 0:
#        return 1
#    return base * calculaPotencia(base, expoente - 1)

#resultado = calculaPotencia(2,5)
#print(resultado)
#Ex4:
#def inverteString(x):
#    if len(x) <= 1:
#        return x
#    return x[-1] + inverteString(x[:-1])
#result = inverteString("Receba")
#print(result)
#ex5
#def somaLista(num):
#    if len(num) == 0:
#        return 
#    return num[0] + somaLista(num[1:])

#Exemplo de recursividade:

#def fatorial(n):
#   if n == 0 or n == 1
#       return 1
#   return n * fatorail(n-1)

def ContagemRegressiva(x):
    if x == 0:
        return 0
    print(x)
    return ContagemRegressiva(x-1)

result = ContagemRegressiva(8)
print(result)