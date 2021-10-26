from random import shuffle

def cria_pecas():

    pieces = []#lista que guarda todas as peças

    # cria as peças do dominó 
    for n1 in range(0,7):
        for n2 in range(0,7):
            if [n2,n1] not in pieces: #impede que surjam peças iguais
                piece = [n1]
                piece.append(n2)
                pieces.append(piece)

    shuffle(pieces)

    return pieces
