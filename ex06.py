verificacao = True
while verificacao:
    produto = 1
    valor = int(input('Informe um número inteiro positivo: '))
    if valor > 0:
        for i in range (valor, 0, -1):
            produto *= i
            print(i, "X " if i > 1 else "→ ", end='')
        print(produto)
        verificacao = False
    else:
        print('Valor inválido')
