#Ex 1:

distanciaPercorrida = int(input("Qual foi a distância percorrida?: "))
consumoTotal = int(input("Qual foi o gasto em gasolina?: "))

mediaDeConsumo = (distanciaPercorrida / consumoTotal)
print("A media de consumo foi de ", mediaDeConsumo)


#Ex 2:

nomeVendedor = input("Digite o seu nome: ")

salarioFixo = float(input("Digite o seu salário: "))

totalVendaMes = float(input("Digite o total em reais de suas vendas feitas: "))

salarioFinalMes = float(totalVendaMes * 0.15) + salarioFixo

print("Vendedor: ", nomeVendedor, "\nSalário fixo: ", salarioFixo, "\nSalário final do mês: ", salarioFinalMes)

#Ex 3:

cotacaoDolar = float(input("Digite a cotação atual do dólar: "))
quantidadeDolar = float(input("Digite a quantidade de dolares que possui: "))

conversaoFinal = quantidadeDolar * cotacaoDolar

print("Sua quantidade final em reais é ", conversaoFinal)

#Ex 4: 

valorDepositado = float(input("Digite o valor depositado: "))

rendimento = (valorDepositado * 0.070) + valorDepositado

print("O rendimento final é de ", rendimento)