numero = int(input('Informe o número: '))
c = 0
while c <= numero:
    if c % 2 == 0:
        print(c, '→ ', end='')
    c += 1
print('Fim!')