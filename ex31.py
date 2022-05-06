var = float(input(("Quantos dias alugados? ")))
var1 = float(input("Quantos Km rodados? "))

var3= var * 60 + var1 * 0.15

print("O total a pagar é de R${}" .format(var3))