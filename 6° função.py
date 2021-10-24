def adiciona_na_mesa(piece, table):

    last_peace = len(table)-1
    inv_piece = [0,0]

    # se a mesa estiver vazia
    if table == []:
        table.append(piece)

    # se a peça escolhida encaixar na peça do início da lista
    # mas tiver que inverter
    elif piece[0] == table[0][0]:
        inv_piece[0] = piece[1]
        inv_piece[1] = piece[0]
        new_table = [inv_piece]
        for p in table:
            new_table.append(p)
        table = new_table

    # se a peça escolhida encaixar na peça do início da lista
    elif piece[1] == table[0][0]:
        new_table = [piece]
        for p in table:
            new_table.append(p)
        table = new_table

    # se a peça escolhida encaixar na peça do final da lista
    elif piece[0] == table[last_peace][1]:
        table.append(piece)

     # se a peça escolhida encaixar na peça do final da lista
     # mas tiver que inverter
    elif piece[1] == table[last_peace][1]:
        inv_piece[0] = piece[1]
        inv_piece[1] = piece[0]
        table.append(inv_piece)
    
    
    return table