print('''OPÇÕES:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
j=int(input('Qual a sua jogada ? '))
if j > 3 or j < 0:
    print('Comando Inválido!')
else:
    from random import randint
    n=randint(1,3)
    from time import sleep
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO !!!')
    sleep(1)
    print('='*31)
    if j == 1 and n == 3:
        print('Jogador escolheu Pedra\nComputador escolheu Tesoura\nJogador GANHOU!')
    elif j == 3 and n == 2:
        print('Jogador escolheu Tesoura\nComputador escolheu Papel\nJogador GANHOU!')
    elif j == 2 and n == 1:
        print('Jogador escolheu Papel\nComputador escolheu Pedra\nJogador GANHOU!')
    elif j == 1 and n == 1:
        print('Jogador escolheu Pedra\nComputador escolheu Pedra\nEMPATE!')
    elif j == 2 and n == 2:
        print('Jogador escolheu Papel\nComputador escolheu Papel\nEMPATE!')
    elif j == 3 and n == 3:
        print('Jogador escolheu Tesoura\nComputador escolheu Tesoura\nEMPATE!')
    elif j == 3 and n == 1:
        print('Jogador escolheu Tesoura\nComputador escolheu Pedra\nJogador PERDEU!')
    elif j == 2 and n == 3:
        print('Jogador escolheu Papel\nComputador escolheu Tesoura\nJogador PERDEU!')
    elif j == 1 and n == 2:
        print('Jogador escolheu Pedra\nComputador escolheu Papel\nJogador PERDEU!')
print('='*31)