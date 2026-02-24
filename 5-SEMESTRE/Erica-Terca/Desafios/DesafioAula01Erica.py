print("-----------------------------------------------------")
print("Bem vindo(a) ao verificador de final de semana!")
dia = int(input("Por favor, digite o dia desejado: "))
x = [1,8,15,22]
y = [4,11,18,25]
z = [5,12,19,26]
match dia:
    case d if d % 7 == 0 and d < 30:
        print("Este dia é um sábado nos meses: Fevereiro e Março.")
    case d if d in x:
        print("Este dia é um domingo nos meses: Fevereiro e Março.")
    case 29:
        print("Este dia é um domingo no mês de Março.")
    case d if d in y:
        print("Este dia é um sábado no mês de Abril.")
    case d if d in z:
        print("Este dia é um domingo no mês de Abril.")
    case _:
        if( 31 < d or d < 0):
            print("O dia não existe")
        else:
            print("Este dia é um dia de semana. ")
print("-----------------------------------------------------")
