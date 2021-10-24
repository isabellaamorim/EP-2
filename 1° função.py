from random import shuffle

def make_pieces(l_pieces):

    # cria as peças do dominó
    for n1 in range(0,7):
        for n2 in range(0,7):
            if [n2,n1] not in l_pieces: #impede que surjam peças iguais
                l_pieces.append([n1,n2])

    shuffle(l_pieces)

    return l_pieces
    
    