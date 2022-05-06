frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()#vai_criar_uma_divisão_nos_espaços.Gera_lista_em_cada_palavra
junto = "".join(palavras)
inverso = frase[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")