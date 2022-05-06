from random import randint
from time import sleep
computador = randint(0, 5) #faz o pc sortear o número
print('-=-' * 20)
print("Vou pensar em um número entre 0 e 5. TENTE ADIVINHAR!")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? ")) #jogador tenta adivinhar
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("Parabéns! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}!" .format(computador, jogador))