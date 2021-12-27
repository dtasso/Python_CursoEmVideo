frase = 'Curso em Video Python'
print(frase[15:])
print(frase[::2])
print(frase[0:22:2])
print(frase[0:])
print(frase[:23])
print(frase.find('Curso'))
print(frase.lower().find('video'))
print(len(frase))
print(frase.count('o',0,13))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python','Android'))
frase = frase.replace('Python','JS')
print(frase)
frase = '   curso em video python  '
print(frase)
print(frase.strip())

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis
condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et
netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et,
sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing.""")
