from random import randint

n = 7
a = 0

for i in range(n):
    num_aleat = randint(0, 50)
    if num_aleat > a and num_aleat <= 40:
        a = num_aleat

print(a)