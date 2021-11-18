from random import randint
from time import sleep

computador = randint(0, 10)
count = 1

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2.5)

while jogador != computador:
    jogador = int(input('Número errado tente novamente.'))
    count += 1

print('Você conseguiu me vencer o número pensado foi {} e você usou {} chances.'.format(computador, count))