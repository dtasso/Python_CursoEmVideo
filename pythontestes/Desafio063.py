fsequence = int(input('Digite quantos números da sequência de fibonnaci deseja mostrar: '))
n1 = 0
n2 = 1
print('{} -> {}'.format(n1, n2), end = '')
count = 3
while count <= fsequence:
    n3 = n1 + n2
    print(' -> {}'.format(n3), end = '')
    n1 = n2
    n2 = n3
    count += 1
print(' fim')