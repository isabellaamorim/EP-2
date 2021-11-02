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

# Cria ordem de jogadas aleatório
ordem_jogadores = embaralha_jogaderes(n_jogadores)

# loop q se repete até um jogador não ter peças
while 0 == 0:
    # Mostra peças ao jogador 0 
    print('Essas são suas peças:')
    print(dicionario_pecas['jogadores'][0])

    # Define e printa a mesa inicial 
    mesa = []
    print()
    print('MESA: {}'.format(mesa))
