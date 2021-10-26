#Função que soma os pontos a cada rodada. Quanto pontos == 0 há um ganhador. 
def soma_pecas(pecas):

    pontos = 0 

    for peca in pecas: 
        pontos += peca[0] + peca[1]

    return pontos
    