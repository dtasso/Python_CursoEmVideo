n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

if n1 > n2 or n1 > n3 and n2 > n3:
    print('O maior é {} e o menor é {}'.format(n1,n3))
elif n1 > n2 or n1 > n3 and n3 > n2:
    print('O maior é {} e o menor é {}'.format(n1,n2))
elif n2 > n1 or n2 > n3 and n1 > n3:
    print('O maior é {} e o menor é {}'.format(n2,n3))
elif n2 > n1 or n2 > n3 and n3 > n1:
    print('O maior é {} e o menor é {}'.format(n2,n1))
elif n3 > n1 or n3 > n2 and n1 > n2:
    print('O maior é {} e o menor é {}'.format(n3,n2))
elif n3 > n1 or n3 > n2 and n2 > n1:
    print('O maior é {} e o menor é {}'.format(n3,n1))