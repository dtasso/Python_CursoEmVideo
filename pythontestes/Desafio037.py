num = int(input('Digite um número inteiro: '))
print('Digite a base a qual quer converter: ')
print('- 1 para binário')
print('- 2 para octal')
print('- 3 para hexadecimal')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')