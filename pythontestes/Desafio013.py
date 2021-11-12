sal = float(input('Digite seu salário em reais: '))
#print('Seu novo salário, após o aumento de 15% será de R${:.2f}'.format(sal*1.15))
saln = sal + (sal * 15 / 100)
print('Seu novo salário, após o aumento de 15% será de R${:.2f}'.format(saln))