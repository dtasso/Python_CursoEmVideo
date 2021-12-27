n = count = soma = 0
# n = int(input('Digite um número[999 para parar]:))
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        count += 1
        soma += n
#   n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(count, soma))