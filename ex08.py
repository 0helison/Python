valor = int(input('Digite um valor para verificar se ele é primo: '))
c = 1
i = 0
while c <= valor:
    if valor % c == 0:
        i += 1
    c += 1
if i == 2:
    print(f'O número {valor} é primo!')
else:
    print(f'O número {valor} não é primo!')