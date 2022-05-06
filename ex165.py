try:
  a = int(input("Numerador: "))
  b = int(input("Denominador: "))
  r = a / b
except:
  print("Infelizmente tivemos um problema!  :(")
else:
  print(f"O resultado é {r}!")
finally:
  print("Volte sempre! Muito obrigado")