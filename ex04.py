lista = [15, 2, 44, 7, 25, 13, 9]
max_valor = min_valor = lista[0]
print(lista)

for num in lista:
    if num > max_valor:
        max_valor = num
    if num < min_valor:
        min_valor = num
print(f'O maior valor é {max_valor} e o menor é {min_valor}!')