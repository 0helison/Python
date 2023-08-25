lista = [16, 21, 43, 7, 24, 36, 10, 3, 12]
print(lista)
soma_pares = total_pares = 0
for num in lista:
    if num % 2 == 0:
        soma_pares += num
        total_pares += 1
media = soma_pares / total_pares
print(f' A média é igual a {media}!')