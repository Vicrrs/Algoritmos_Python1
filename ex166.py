try:
  a = int(input("Numerador: "))
  b = int(input("Denominador: "))
  r = a / b
except Exception as erro:
  print(f"Problema do erro foi {erro.__class__}")
else:
  print(f"O resultado é {r}!")
finally:
  print("Volte sempre! Muito obrigado")