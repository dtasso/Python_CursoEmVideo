km = int(input('Digite quantos KM de distância: '))

if km <= 200:
    valor = km * 0.5
    print('O Preço da passagem é de R${:.2f}'.format(valor))
else:
    valor = km * 0.45
    print('O preço da passagem é de R${:.2f}'.format(valor))