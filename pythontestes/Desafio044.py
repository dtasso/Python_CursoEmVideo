valor = float(input('Digite o valor: '))
print('Insira a condição de pagamento: ')
print('[1] - À vista, Dinheiro ou Cheque (10% de desc.)')
print('[2] - À vista no cartão (5% de desconto)')
print('[3] - Em até 2x no cartão (Preço normal)')
print('[4] - Em 3x ou mais (20% de juros)')
opcao = int(input(''))

if opcao == 1:
    print('O valor a ser pago vai ser de R${:.2f} a vista, dinheiro ou cheque'.format(valor * 0.9))
elif opcao == 2:
    print('O valor a ser pago vai ser de R${:.2f} a vista, no cartão'.format(valor * 0.5))
elif opcao == 3:
    print('O valor a ser pago vai ser de R${:.2f} em até 2x no cartão'.format(valor))
elif opcao == 4:
    print('O valor a ser pago vai ser de R${:.2f} em 3x ou mais'.format(valor * 1.2))
