from math import sin, cos, tan, radians
ang = float(input('Digite o valor do ângulo o qual deseja descobrir o seno, cosseno e tangente: '))
coss = cos(radians(ang))
seno = sin(radians(ang))
tangent = tan(radians(ang))
print('O valor do cosseno de {} é {:.2f}, o seno é {:.2f} e a tangente é {:.2f}'.format(ang, coss, seno, tangent))