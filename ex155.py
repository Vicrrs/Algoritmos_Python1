#Onde b e c são escopo local e a escopo global
def teste(b):
  b += 4
  c = 2
  print(f"A dentro vale {a}")
  print(f"B dentro vale {b}")
  print(f"C dentro vale {c}")


a = 5
teste(a)
print(f"A fora vale {a}")
#no entando b e c nao podem ser lidas aq pois sao variaveis locais de def