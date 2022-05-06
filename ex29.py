var = float(input(("Qual é o salário do Funcionário? R$")))

var1 = var + (var * 15/100)

print("Um funcionário que ganhava R$ {}, com 15% de aumento, passa a receber R$ {}" .format(var, var1))