# 
def verifica_ganhador(jogador_pecas): 

    for jogador, pecas in jogador_pecas.items():

        if pecas == []: 
            return jogador

    return -1
    