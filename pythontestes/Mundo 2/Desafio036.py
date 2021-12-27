casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos_prestacao = int(input('Em quantos anos irá pagar?: '))

valor_prest = casa / (anos_prestacao * 12)
ver_emprest = salario * 0.3

if valor_prest >= ver_emprest:
    print('Empréstimo negado.')
else:
    print('Parabéns o empréstimo foi aprovado')