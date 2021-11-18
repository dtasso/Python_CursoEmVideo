sexo = str(input('Digite seu sexo: ')).strip()
while sexo not in 'MmFf':
    sexo = str(input('Entrada inválida, digite novamente: '))
print('O Sexo {} foi registrado com sucesso.'.format(sexo))