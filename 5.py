def posicoes_possiveis(table, player_pieces):

    possibilities = []

    if table == []:
        i = 0
        while i < len(player_pieces):
            possibilities.append(i)

    else:
        num1 = table[0][0]
        num2 = table[len(table)-1][1]

        i = 0
        # while i < player_pieces:

            # if piece[0] in num1 or piece[0] in num2 or piece[1] in num1 or piece[1] in num2:
