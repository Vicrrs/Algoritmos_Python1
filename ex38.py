import math
var = int(input("Digite um valor para um ângulo em graus: "))
seno = math.sin(math.radians((var)))
cosseno = math.cos((math.radians(var)))
tangente = math.tan(math.radians((var)))

print("Os resultados para o ângulo {} valem em: \n Seno {:.2f} \n Cosseno {:.2f} \n Tangente {:.2f}" .format(var, seno, cosseno, tangente))