frase = str(input('Digite a frase: ')).strip().upper()
print('A letra A aparece {} Vezes na frase.'.format(frase.count('A')))
print('A primeira letra a apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra a apareceu na posição {}.'.format(frase.rfind('A')+1))
