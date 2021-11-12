from time import sleep

vel = int(input('Digite a velocidade atual do carro: '))

print('Processando...')
sleep(1.5)

if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado e a multa é de: {}'.format(multa))
else:
    print('Parabéns, você está em uma velocidade aceitável')