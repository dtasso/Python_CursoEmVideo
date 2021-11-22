from types import SimpleNamespace


maior = 0
menor = 0
count = 0
m1 = 0
continuar = 'Sim'

while continuar in 'SimSIMsim':
    valor = int(input('Digite um valor: '))
    if menor == 0:
        menor = valor
    elif valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
    m1 += valor
    count += 1
    continuar = str(input('Deseja continuar? '))
media = m1 / count
print('A média foi de {}, o maior valor foi {} e o menor valor foi {}.'.format(media, maior, menor))