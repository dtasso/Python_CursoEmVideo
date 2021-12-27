idadem = 0
idadeh = 0
mulheres = 0

for c in range(1, 5):
    print('----- {}ª pessoa -----'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    idadem += idade
    '''if p == 1 and sexo in 'Mm':
            idadem = idade
            maisvelho = nome'''
    if sexo in 'Mm' and idade > idadeh:
        maisvelho = nome
        idadeh = idade
    elif sexo in 'fF' and idade < 20:
        mulheres += 1

mediaidade = idadem / 4

print('A média de idade do grupo é {}'.format(idadem/4))
print('A média de idade do grupo é {}'.format(mediaidade))
print('O nome do homem mais velho é {} com {} anos.'.format(maisvelho,idadeh))
print('E existem {} mulheres com menos de 20 anos.'.format(mulheres))
