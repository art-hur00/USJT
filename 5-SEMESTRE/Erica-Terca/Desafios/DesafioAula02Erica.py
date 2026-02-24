##Importando random para utilizá-lo na escolha do adversário.
import random

#Boas vinda e explicação sobre o jogo.
print("Bem vindo ao super desafio de: PEDRA, PAPEL OU TESOURA!! \nEspero que esteja preparado! \n")
print("REGRAS: Este jogo é um clássico pedra papel e tesoura, onde você pode escolhor 3 opções, Pedra, Papel ou Tesoura, e seu adversário também seleciona uma delas.\nCada opção tem vantagem contra uma e desvantagem com outra opção!" \
"Exemplos: Papel vence Pedra e perde para tesousa, já a tesoura perde para pedra e vence papel.\nCada vitória conta um ponto,cada derrota perde um ponto. \nVocê pode para quando quiser.\nBom jogo!")

#Um if e um input para começar o programa, ambos as opções levam ao mesmo lugar, por efeitos cômicos
comecar = input("\nDeseja começar a jogar? (s/n)").lower()
if comecar == "s":
    print("Então vamos lá \n")
else:
    print("Sério?")
    print("Então por que abriu o programa? \nJoga logo.")

#A variável pontuacao é declarada aqui para que a mesma não seja declarada como 0 toda vez que o laço recomeçe.
pontuacao = 0

#Dentro deste while, está todo o código do jogo em sí. O while é declarado como True afinal para o funcionamento do código não é necessário uma condição especifica.
while True:       
   
    #Aqui se é declarado as váriaveis que guardam a escolha do usuário, criam uma lista de escolhas que via random, e armazena-se a escolha 'aleatória' da cpu.  
    arma = input("Selecione sua arma: \nPEDRA\nPAPEL\nTESOURA\nDigite o nome de sua arma:").lower()
    print("\nVocê selecionou ", arma, " boa sorte...\n")
    armaAdversario = ["pedra", "papel","tesoura"]
    escolhaAdversario =  random.choice(armaAdversario)
   
    #Método match para todas as possíveis combinações corretas entre a esccolha do usuário e a criada via random.choice.
    match arma:
        case "pedra":
            if escolhaAdversario == "pedra":
                print("Seu adversário selecionou PEDRA... \n\nResultado:EMPATE.\n")
                print("Sua pontuação é ",pontuacao)
            elif escolhaAdversario == "papel":
                print("Seu adversário selecionou PAPEL... \n\nResultado:DERROTA.\n")
                pontuacao -= 1
                print("Sua pontuação é ",pontuacao)
            elif escolhaAdversario == "tesoura":
                print("Seu adversário selecionou TESOURA... \n\nResultado:VITÓRIA!.\n")
                pontuacao += 1
                print("Sua pontuação é ",pontuacao) 
        case "papel":
            if escolhaAdversario == "pedra":    
                print("Seu adversário selecionou PEDRA... \n\nResultado:VITÓRIA.\n")
                pontuacao += 1
                print("Sua pontuação é ",pontuacao)
            elif escolhaAdversario == "papel":
                print("Seu adversário selecionou PAPEL... \n\nResultado:EMPATE.\n")
            else:
                print("Seu adversário selecionou TESOURA... \n\nResultado:DERROTA.\n")
                pontuacao -= 1
                print("Sua pontuação é ",pontuacao) 
        case "tesoura":
            if escolhaAdversario == "pedra":    
                print("Seu adversário selecionou PEDRA... \n\nResultado:DERROTA.\n")
                pontuacao -= 1
                print("Sua pontuação é ",pontuacao)
            elif escolhaAdversario == "papel":
                print("Seu adversário selecionou PAPEL... \n\nResultado:VITÓRIA!.\n")
                pontuacao += 1
                print("Sua pontuação é ",pontuacao)
            else:
                print("Seu adversário selecionou TESOURA... \n\nResultado:EMPATE.\n")
                print("Sua pontuação é ",pontuacao)
   
    #Este input e o if servem para dar a opção ao usuário de sair ou continuar no loop while, caso ele saia o programa se encerra.
    continuar = input("Deseja continuar? (s/n)")
    if continuar == "s":
        continue
    else:
        print("Obrigado por jogar!")
        print("\nSua pontuação final é ", pontuacao, "\nParabéns!")
        break

#Construi este software usando loops (while),e condicionais como if e match case. Utilizei lowe,random.choice como métodos e a biblioteca random.
#Começei o código com o import, e com um print onde expliquei as regras, e como funciona o jogo Pedra, Papel e Tesoura. Depois iniciei uma condicional if para que o jogo em sí só começe quando o usuário 
#digitar se quer ou não entrar no jogo(Por efeito cômico ambas as opções levam para o começo do jogo). Declaro a variável 'pontuacao' fora do loop while para que a mesma não seja declarada zero toda a vez que o loop se reinicie,
#Declaro um loop while onde construí a parte principal do algoritmo do jogo, nele faço as variáveis que armazenam os valores escolhidos pelo usuário, e gero via random.choise em uma lista um valor 'aleatório' dentro das possibílidades da lista,
#e então uso o condicional match case para comparar os valores do usuário com os valores da máquina, e assim gerar pontuação positiva ou negativa. Após o match case usei outro condicional if para dar a opçaõ de continuar o jogo(se manter no laço while),
# ou sair do jogo(encerrar o programa) para o usuário. Caso o mesmo saia ele recebe sua pontuação final, diferento dos resultados na match case, onde a pontuação era parcial. 