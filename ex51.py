from random import randint
computador = randint(0, 5) #faz o pc sortear o número
print('-=-' * 20)
print("Vou pensar em um número entre 0 e 5. TENTE ADIVINHAR!")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? ")) #jogador tenta adivinhar
if jogador == computador:
    print("Parabéns! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}!" .format(computador, jogador))