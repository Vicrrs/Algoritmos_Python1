n1 = float(input("A primeira nota do aluno foi : "))
n2 = float(input("A segunda nota do aluno foi: "))

m = (n1+n2)/2

print("A média entre {} e {} é igual a {}" .format(n1, n2, m))
if m >= 6.0:
    print("Sua média foi boa, parabéns! ")
else:
    print("Sua média não foi boa, estude mais!!")