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
