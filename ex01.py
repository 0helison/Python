i = 1
soma_notas = 0
for i in range(1, 4):
    nota = float(input(f'Informe a {i}º nota do aluno: '))
    soma_notas += nota
    i += 1
media = soma_notas / (i-1)
print(f'A média do aluno é igual a {media}!')