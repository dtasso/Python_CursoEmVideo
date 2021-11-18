from random import randint
from time import sleep

itens = ('null','Pedra', 'Papel', 'Tesoura')
computador = randint(1,3)
print('-='*19)
print('-='*4,'Bem-vindo ao jokenpô','-='*4)
print('-='*19)

print('''Digite sua opção: 
[1] - Pedra
[2] - Papel
[3] - Tesoura''')

jogador = int(input('Qual é sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-='*19)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*19)

if computador == 1: #computador jogou pedra
    if jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Venceu')
    elif jogador == 3:
        print('Computador Venceu')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('Empate')
    elif jogador == 3:
        print('Jogador Venceu')
    else:
        print('Jogada inválida')
elif computador == 3:
    if jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador venceu')
    elif jogador == 3:
        print('Empate')
    else:
        print('Jogada inválida')
