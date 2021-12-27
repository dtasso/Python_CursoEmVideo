termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
quantidade_termos = int(input('Digite a quantidade de termos que deseja mostrar, ou 0 se não quiser mostrar nenhum termo: '))
count = 1
total = 0
while quantidade_termos != 0:
    total = total + quantidade_termos
    while count <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        count +=1
    print('pausa')
    mais = int(input('Quantos termos deseja mostrar a mais? '))
print('A Progressão acabou, foram mostrados {} termos da PA.'.format(total))