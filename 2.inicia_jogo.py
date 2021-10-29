#Função para ínicio do jogo.
def inicia_jogo(n_jogadores, lista_pecas):

    #Define variáveis padrão

    jogador0 = []
    jogador1 = []
    jogador2 = []
    jogador3 = []
    monte = []
    dic_inicio = {'jogadores':{},'monte':[] , 'mesa':[]}

    #Desconsidera casos inválidos

    if (n_jogadores != 2) or (n_jogadores != 3) or (n_jogadores != 4): 
        return 'Opção inválida. Escolha entre 2, 3 ou 4 jogadores.'

    #Caso de 2 jogadores

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

    #Caso de 3 jogadores

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

    #Caso de 4 jogadores

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
        

        



