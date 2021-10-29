from random import shuffle

#Função 1: cria peças do jogo. 

def cria_pecas():

    pieces = [] #lista que guarda todas as peças

    # cria as peças do dominó 
    for n1 in range(0,7):
        for n2 in range(0,7):
            if [n2,n1] not in pieces: #impede que surjam peças iguais
                piece = [n1,n2]
                pieces.append(piece)

    shuffle(pieces)

    return pieces

#Função 2: para ínicio do jogo - distribuição de peças.

def inicia_jogo(n_jogadores, lista_pecas):

    #Define variáveis padrão

    jogador0 = []
    jogador1 = []
    jogador2 = []
    jogador3 = []
    monte = []
    dic_inicio = {'jogadores':{},'monte':[] , 'mesa':[]}

    #Desconsidera casos inválidos

    if (n_jogadores != 2) and (n_jogadores != 3) and (n_jogadores != 4): 
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

#Função 3: verifica ganhador a cada rodada
def verifica_ganhador(jogador_pecas): 

    for jogador, pecas in jogador_pecas.items():

        if pecas == []: 
            return jogador

    return -1

#Função 4: soma os pontos a cada rodada. Quando pontos == 0 há um ganhador
def soma_pecas(pecas):

    pontos = 0 

    for peca in pecas: 
        pontos += peca[0] + peca[1]

    return pontos

#Função 5: verifica as possibilidades de peças que podem ser jogadas por rodada. 
def posicoes_possiveis(table, player_pieces):

    possibilities = []# lista que recebe os valores de retorno da função

    # possibilidades de jogo em mesa sem peça
    if table == []:
        i = 0
        while i < len(player_pieces):
            possibilities.append(i)
            i += 1

    # possibilidades de jogo em mesa com pelo menos uma peça
    else:
        # números na estremidade da mesa
        num1 = table[0][0]
        num2 = table[len(table)-1][1]

        # caucula as posições das peças jogáveis
        i = 0
        for piece in player_pieces:

            if num1 in piece or num2 in piece:
                possibilities.append(i)
            i += 1

    return possibilities

#Função 6: função que coloca peças na mesa
def adiciona_na_mesa(piece, table):

    last_peace = len(table)-1
    inv_piece = [0,0]

    # se a mesa estiver vazia
    if table == []:
        table.append(piece)

    # se a peça escolhida encaixar na 1° peça da mesa
    # mas tiver que inverter
    elif piece[0] == table[0][0]:
        inv_piece[0] = piece[1]
        inv_piece[1] = piece[0]
        new_table = [inv_piece]
        for p in table:
            new_table.append(p)
        table = new_table

    # se a peça escolhida encaixar na 1° peça da mesa
    elif piece[1] == table[0][0]:
        new_table = [piece]
        for p in table:
            new_table.append(p)
        table = new_table

    # se a peça escolhida encaixar na última peça da mesa
    elif piece[0] == table[last_peace][1]:
        table.append(piece)

     # se a peça escolhida encaixar na última peça da mesa
     # mas tiver que inverter
    elif piece[1] == table[last_peace][1]:
        inv_piece[0] = piece[1]
        inv_piece[1] = piece[0]
        table.append(inv_piece)
    
    return table
    
