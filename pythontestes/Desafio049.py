print('-=-'*8)
print('-=-'*2,' Tabuada ','-=-'*2)
print('-=-'*8)

n = int(input('Digite um número inteiro: '))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n,c,n*c))