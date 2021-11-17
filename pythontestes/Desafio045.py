from random import randint

print('-='*19)
print('-='*4,'Bem-vindo ao jokenpô','-='*4)
print('-='*19)

print('Digite sua opção: ')
print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')

opcao_jogador = int(input(''))
opcao_computador = randint(1,3)

print(opcao_computador)

if opcao_computador == 1 and opcao_jogador == 1 or opcao_jogador == 2 and opcao_computador == 2 or opcao_computador == 3 and opcao_jogador == 3:
    print('Deu empate!')
elif opcao_computador == 1 and opcao_jogador == 2 or opcao_jogador == 3 and opcao_computador == 2 or opcao_jogador == 1 and opcao_computador == 3:
    print('O jogador ganhou!')
elif opcao_computador == 1 and opcao_jogador == 3 or opcao_computador == 2 and opcao_jogador == 1 or opcao_computador == 3 and opcao_jogador == 2:
    print('O Computador Ganhou!')

