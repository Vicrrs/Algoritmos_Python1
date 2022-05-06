#Criando uma dosctring para meu contador
from time import sleep

def contador(i, f, p):
  """
  -> Faz contagem e mostra na tela
  para i: inicio da contagem
  para f: fim da contagem
  para p: passa a passo da contagem
  return: sem retorno
  """
  c = i
  while c <= f:
    print(f"{c} ", end= ' ')
    sleep(0.5)
    c += p
  print(" -> FIM!")

help(contador)