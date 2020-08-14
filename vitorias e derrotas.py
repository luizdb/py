vitorias = 0
derrotas = 0
terminou = False
while not terminou:
    resposta = str(input('Voce ganhou ou perdeu (v ou d)'))
    if resposta == 'v':
        vitorias += 1
    if resposta == 'd':
        derrotas += 1
    r = str(input('Voce terminou hoje?'))
    if r == 's':
        terminou = True
print('Voce teve {} vitorias e {} derrotas hoje'.format(vitorias, derrotas))





