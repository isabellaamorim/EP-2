def soma_pecas(player_pieces):
    
    amount = 0
    for piece in player_pieces:
        for number in piece:
            amount += number
    
    return amount
