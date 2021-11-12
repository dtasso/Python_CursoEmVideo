ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    if ano <= 100:
        print('Ano Bissexto')
    elif ano > 100 and ano <= 400 and ano % 100 == 0:
        print('Ano Bissexto')
    elif ano > 400 and ano % 400 == 0:
        print('Ano Bissexto')
    else:
        print('Não é ano bissexto')
elif ano % 4 != 0:
    print('Não é ano bissexto')
