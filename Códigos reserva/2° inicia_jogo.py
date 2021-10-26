def inicia_jogo(num_players, pieces):
    pack =[]
    dic_game = {
     
     }
    if num_players < 2 or num_players > 4:
        return 'Número de jogadore deve ser 2, 3 ou 4.'
    else:
        for i in range(0,5):
            pack = pieces[0:6]
            dic_game['jogadoers'] = {i: pack}

    lista =  [[0, 1], [4, 6], [0, 3], [0, 4], [6, 6], [0, 6], [1, 1], [1, 2], [0, 0], [1, 4], [1, 5], [1, 6], [2, 2], [3, 6], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [2, 3], 
[3, 5], [4, 4], [4, 5], [0, 2], [5, 5], [5, 6], [0, 5]]