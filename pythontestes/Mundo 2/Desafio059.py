n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
resultado = 0

print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa''')

opcao = int(input('Digite uma opção: '))

while opcao != 5:
    if opcao == 1:
        resultado = n1 + n2
        print(resultado)
    if opcao == 2:
        resultado = n1 * n2
        print(resultado)
    if opcao == 3:
        if n1 > n2:
            resultado = n1
        if n2 > n1:
            resultado = n2
        print(resultado)
    if opcao == 4:
        n1 = float(input('Digite um novo primeiro número: '))
        n2 = float(input('Digite um novo segundo número: '))
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa''')
    opcao = int(input('Digite agora, qual operação quer fazer ou 5 para sair.'))
print('FIM')
