linha1 = input()
linha2 = input()

cod1 = linha1.split(" ")[0]
qtde1 = int(linha1.split(" ")[1])
valor1 = float(linha1.split(" ")[2])

cod2 = linha2.split(" ")[0]
qtde2 = int(linha2.split(" ")[1])
valor2 = float(linha2.split(" ")[2])

total = (qtde1 * valor1) + (qtde2 * valor2)

print("VALOR A PAGAR: R$ %0.2f" %total)