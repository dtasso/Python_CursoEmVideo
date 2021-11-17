casa = float(input('Digite o valor da casa'))
salario = float(input('Digite o valor do seu salário'))
anos_prestacao = int(input('Em quantos anos irá pagar?'))

meses_prest = anos_prestacao * 12
valor_prest = casa / meses_prest
ver_emprest = salario * 0.3

if valor_prest > ver_emprest:
    print('Empréstimo negado.')
else:
    print('Parabéns o empréstimo foi aprovado')