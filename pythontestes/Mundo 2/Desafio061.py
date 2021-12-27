ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = int(input('Quantos termos deseja mostra?: '))
decimo = ptermo + (termos - 1) * razao

while ptermo < (decimo + razao):
    print(ptermo, end=' => ')
    ptermo += razao
print('Acabou')
