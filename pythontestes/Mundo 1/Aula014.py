'''c = 1

while c <= 10:
    print(c)
    c += 1
print('fim')

n=1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
'''

par = impar = 0
while n != 0:
    n = int(input('Digite um valor se quiser parar, digite 0: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))