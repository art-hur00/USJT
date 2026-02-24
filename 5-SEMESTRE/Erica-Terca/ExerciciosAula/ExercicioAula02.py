print("Bem vindo ao Tabuador")
while True:
    num = int(input("Digite o número que deseja calcular: "))
    max = num * 11
    for i in range(0,max, num):
        print(i)
    parada = input("Deseja continuar? (s/n)")
    if parada == "s":
        continue
    elif parada == "n":
        print("Obrigado por usar o Tabuador!")
        print("Encerrando o programa...")
        break
    else:
        print("Error: command not found")
        print("Encerrando o programa...")

##Neste programa quando o usuário loga ele recebe uma mensagem de bem vindo, que deve estar fora do laço para que a mesma não fique se repetindo.
##O laço while é sempre True, afinal quase todo o código está dentro dele. Por começo são declaradas apenas duas váriaveis, a num, que ira armazenar o número a ser calculado, e a max, que calcula o valor limite da tabuada,
##ou seja, o num multiplicado por 11. Dentro do laço for se é declarado i que em range começa no número 0, vai até max(num*11) para assim cobrir todas as somas entre 0 e 10, e a incrementação
##que é o próprio num. dentro deste for há um print(i), para que a tabuada seja impressa no console. Quando o laço for se conclui se é declada a terceira váriavel, parada, uma String, que armazena a resposta do usuário sobre a continuação ou não no programa.
##O if serve para caso o usuário deseja continuar, com apenas um continue o laço while se repete. Já o elif é acionado caso o usuário seleciona 'n', o programa se encerra. Também há um else, para caso o usuário digite algo diferente de 's' ou 'n', 
##neste else o programa para