ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = ptermo + (10-1) * razao

for c in range (ptermo, decimo + razao, razao):
    print('{} '.format(c), end=' =>')
print('Acabou')