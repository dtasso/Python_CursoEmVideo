from random import sample, shuffle
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input("Digite o nome do quarto aluno: ")
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
#print('O aluno escolhido para limpar a lousa foi: {} e a ordem de apresentação será: {}'.format(sample([n1, n2, n3, n4], k=1),sample([n1, n2, n3, n4], k=4)))