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

for i in range(2,5):
    for m in range(0,5):
        print(embaralha_jogaderes(i))