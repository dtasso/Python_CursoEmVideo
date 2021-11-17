print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo')
    if r1 == r2 == r3:
        print('É um triângulo Equilátero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('É um triângulo Isósceles')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Todos os lados são diferentes')
else:
    print('Os segmentos acima não podem formar um triângulo')

