from random import choice
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input("Digite o nome do quarto aluno: ")
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

#from random import sample
#sel = sample([n1, n2, n3, n4], k=1)
#print('O aluno escolhido foi: {}'.format(sel))