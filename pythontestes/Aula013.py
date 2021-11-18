n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)

i = int(input('inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)

s = 0
for c in range (0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O Somatório de todos os valores foi {}'.format(s))

for c in range (0, 6):
    print('Oi')
print('fim')

for c in range (6, 0, -1):
    print(c)
print('fim')