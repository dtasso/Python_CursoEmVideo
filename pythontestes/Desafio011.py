la = float(input('Digite a largura da parede: '))
al = float(input('Digite a altura da parede: '))
areap = la * al
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(la, al, areap))
tinta = areap / 2
print('Você irá precisar de {} litros de tinta'.format(tinta))