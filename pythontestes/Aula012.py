nome = str(input('Qual seu nome? '))

if nome == 'Diego':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Mariana':
    print('Seu nome é bem popular no  Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Que nome normal.')



print('Tenha um bom dia {}'.format(nome))