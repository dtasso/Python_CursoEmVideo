ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = ptermo + (10-1) * razao

while ptermo < (decimo + razao):
    print(ptermo, end=' => ')
    ptermo += razao
print('Acabou')

decvar = int(input('Deseja exibir mais quantos termos? '))
decimo = ptermo + (decvar - 1) * razao

while ptermo < (decimo + razao):
    print(ptermo, end = ' => ')
    ptermo += razao
print('Agora realmente acabou')