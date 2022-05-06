import math
var = float(input("Fale um valor para o cateto oposto: "))
var1 = float(input("Fale um valor para o cateto adjacente: "))

co = var
ca = var1
HP = math.sqrt((var)**2 + (var1)**2)

print("O valor do cateto oposto vale {} o valor do cateto adjacente vale {}, assim temos que a hipotenusa vale {}: " .format(co, ca, HP))