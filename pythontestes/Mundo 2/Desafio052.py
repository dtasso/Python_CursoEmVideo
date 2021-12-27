n = int(input('Digite um número inteiro: '))
div = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end = ' ')
        div += 1
    else:
        print('\033[31m', end = ' ')
    print('{} '.format(c), end= ' ')
if div <= 2:
    print('\n\033[mÉ um número primo')
else:
    print('\n\033[mNão é um número primo')