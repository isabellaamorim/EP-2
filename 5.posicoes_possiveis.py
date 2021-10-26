# recebe lista da mesa e peças de um jogador
# retorna 
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
