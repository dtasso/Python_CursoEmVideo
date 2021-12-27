n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('Sua média foi de {:.1f} e você foi reprovado'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi de {:.1f} e você ficou de recuperação'.format(media))
elif media >= 7:
    print('Parabéns, sua média foi de {:.1f} e você foi aprovado'.format(media))