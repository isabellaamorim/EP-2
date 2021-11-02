from random import shuffle

#
#
# Função 7: função enbaralha ordem dos jogadores
def embaralha_jogaderes(n_jogadores):
    ordem_jogada = []
    for i in range(0, n_jogadores):
        ordem_jogada.append(i)

    shuffle(ordem_jogada)

    return ordem_jogada

print(embaralha_jogaderes(4))