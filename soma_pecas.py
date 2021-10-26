def soma_pecas(pecas):

    pontos = 0 

    for peca in pecas: 
        pontos += peca[0] + peca[1]

    return pontos