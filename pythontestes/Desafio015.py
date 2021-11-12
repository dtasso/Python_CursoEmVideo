dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Rodou quantos km? '))
vt = (dias * 60) + (km * 0.15)
print('O preço total a pagar será R${}'.format(vt))
