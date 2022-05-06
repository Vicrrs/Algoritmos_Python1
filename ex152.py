from time import sleep

def contador(i, f, p):
  c = i
  while c <= f:
    print(f"{c} ", end= ' ')
    sleep(0.5)
    c += p
  print(" -> FIM!")

contador(2, 100, 2)