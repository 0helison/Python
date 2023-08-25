qtd = int(input('Quantos valores da sequência de Fibonacci você quer ver? '))
n1 = 0
n2 = 1
print(n1, '→', n2, '→ ', end='')
for c in range(2, qtd):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, '→ ', end='')
    c += 1
print('Fim!')

