import math
#from math import sqrt, floor, ceil #ceil(raiz), sqrt(num), floor(raiz)
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raíz quadrada de {} arredondada pra cima é: {} E arredondada para baixo é: {}'.format(num, math.ceil(raiz), math.floor(raiz)))
