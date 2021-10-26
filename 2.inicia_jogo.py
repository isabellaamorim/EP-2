def inicia_jogo(n_jogadores, lista_pecas):

    jogador0 = []
    jogador1 = []
    jogador2 = []
    jogador3 = []
    monte = []
    mesa = []
    dic_inicio = {'jogadores':{},'monte':[] , 'mesa':[]}

    if n_jogadores == 2:

        for i in range(0,7): 
            jogador0.append(lista_pecas[i])

        for i in range(7,14): 
            jogador1.append(lista_pecas[i])

        for i in range(14,28): 
            monte.append(lista_pecas[i])

        dic_inicio['jogadores'][0] = jogador0
        dic_inicio['jogadores'][1] = jogador1
        dic_inicio['monte'] = monte

    if n_jogadores == 3:

        for i in range(0,7): 
            jogador0.append(lista_pecas[i])

        for i in range(7,14): 
            jogador1.append(lista_pecas[i])

        for i in range(14,21): 
            jogador2.append(lista_pecas[i])

        for i in range(21,28): 
            monte.append(lista_pecas[i])

        dic_inicio['jogadores'][0] = jogador0
        dic_inicio['jogadores'][1] = jogador1
        dic_inicio['jogadores'][2] = jogador2
        dic_inicio['monte'] = monte

    if n_jogadores == 4:

        for i in range(0,7): 
            jogador0.append(lista_pecas[i])

        for i in range(7,14): 
            jogador1.append(lista_pecas[i])

        for i in range(14,21): 
            jogador2.append(lista_pecas[i])

        for i in range(21,28): 
            jogador3.append(lista_pecas[i])

        dic_inicio['jogadores'][0] = jogador0
        dic_inicio['jogadores'][1] = jogador1
        dic_inicio['jogadores'][2] = jogador2
        dic_inicio['jogadores'][3] = jogador3
        dic_inicio['monte'] = []

    return dic_inicio


        

        



