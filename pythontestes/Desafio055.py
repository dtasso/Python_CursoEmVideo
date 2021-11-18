maiorpeso = 0
menorpeso = 0

for p in range (1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maiorpeso = p
        menorpeso = p
    else:
        if peso < menorpeso:
            menorpeso = peso
        if peso > maiorpeso:
            maiorpeso = peso
        
print('O maior peso foi de {} e o menor peso foi de {}'.format(maiorpeso, menorpeso))