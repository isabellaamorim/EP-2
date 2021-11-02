from biblioteca_funções import * 

# Boas vindas
print('\033[47m'+'\033[1m'+'\033[30m'+' Bem vindo ao JOGO DE DOMINÓ '+'\033[0;0m')
print('O objetivo é ser o primeiro jogador a ficar sem peças na mão!')
print()
print('Vamos começar.')
n_jogadores = int(input('Escolha entre 2, 3 ou 4 jogadores: '))
print()

while n_jogadores < 2 or n_jogadores > 4:
    print('Número de jogadores inválido.')
    n_jogadores = int(input('Escolha entre 2, 3 ou 4 jogadores: '))
    print()


# Criação a distribuição de peças
pecas = cria_pecas()
dicionario_pecas = inicia_jogo(n_jogadores, pecas)

# EXEMPLO com 2 jogadores
# dicionario_pecas == {'jogadores': {0: [[0, 5], [3, 5], [4, 4], [3, 4], [0, 3], [6, 6], [1, 3]], 1: [[4, 6], [3, 3], [4, 5], [3, 6], [5, 5], [0, 1], [1, 1]]}, 'monte': [[1, 4], [2, 5], [2, 3], [0, 0], [1, 2], [0, 4], [2, 4], [0, 6], [2, 2], [5, 6], [0, 2], [1, 6], [2, 6], [1, 5]], 'mesa': []}

# Cria ordem de jogadas aleatório
ordem_jogadores = embaralha_jogaderes(n_jogadores)

# loop q se repete até um jogador não ter peças
while 1 == 1:

    for i in ordem_jogadores:
        
        # controla vez do computador ou jogador
        if i == 0:
            # Mostra peças ao jogador 0
            print('Essas são suas peças:')
            print(dicionario_pecas['jogadores'][0])

            # Define e printa a mesa inicial 
            print()
            print('MESA: {}'.format(dicionario_pecas['mesa']))
            print('Escolha a peça: ')
            jogada = int(input())

        else:
            jogada_PC = posicoes_possiveis(dicionario_pecas['mesa'], dicionario_pecas['jogadores'][i])
            print(jogada_PC)

            if len(jogada_PC) > 0:
                dicionario_pecas['mesa'].append(dicionario_pecas['jogadores'][i][jogada_PC[0]])
            #else: