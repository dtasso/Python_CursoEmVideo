frase = str(input('Digite uma frase a verificar se é um palíndromo: ')).strip.upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))

'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
    
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
print(inverso)