s = 0
count = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        s += c
        count += 1
print('A soma de todos os {} valores é {}'.format(count, s))