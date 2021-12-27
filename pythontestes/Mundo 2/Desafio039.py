from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc

if idade > 18:
    print('Já passaram {} anos do tempo de alistamento.'.format(idade - 18))
elif idade == 18:
    print('Está na idade de se alistar, fique ligado.')
else:
    print('Ainda faltam {} anos para o alistamento.'.formate(18 - idade))