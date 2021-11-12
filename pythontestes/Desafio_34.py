sal = int(input('Digite o salário: '))

if sal > 1250:
    sal = sal - (sal * 1.1)
else:
    sal = sal - (sal* 1.15)

print('o aumento vai ser de {}'.format(sal))