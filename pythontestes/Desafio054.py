from datetime import date

anoatual = date.today().year
maioridade = 0

for c in range (1, 8):
    anonasc = int(input('Digite o ano que a {}ª pessoa nasceu: '.format(c)))
    idade = anoatual - anonasc
    if idade >= 21:
        maioridade += 1
print('O número total de pessoas que atingiram a maior idade foi de {}, e {} pessoas ainda não atingiram a maior idade'.format(maioridade, 7 - maioridade))