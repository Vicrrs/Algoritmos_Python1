nome = "Victor" #Variável global


def minha_funcao():
  #bloco interno *é conhecido como corpo da função
  nome = "Jaque" #variavel local
  tupla= (2, 5, 6, 7, 9)
  print(nome)
  print(tupla)
  if nome == "Jaque":
    print("Impressão do bloco interno if")
  for x in tupla:
    print(x)
  

minha_funcao()
print(nome)