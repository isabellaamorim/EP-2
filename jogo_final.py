from biblioteca_funções import * 
from função_cores import *

start = True 

while start: 

    # Boas vindas
    print('\033[47m'+'\033[1m'+'\033[30m'+' Bem vindo ao JOGO DE DOMINÓ '+'\033[0;0m')
    print('O objetivo é ser o primeiro jogador a ficar sem peças na mão!')
    print()
    print('Vamos começar.')
    print('Antes, lembre-se: As peças estão numeradas de 1 a 7')
    print()
    n_jogadores = input('Escolha entre 2, 3 ou 4 jogadores: ')
    print()

    while (n_jogadores != '2') and (n_jogadores != '3') and (n_jogadores != '4'):
        print('Opção inválida. Escolha entre 2, 3 ou 4 jogadores.')
        n_jogadores = input('Escolha entre 2, 3 ou 4 jogadores: ')
        print()

    n_jogadores = int(n_jogadores)

    # Criação a distribuição de peças
    pecas = cria_pecas()
    dicionario_pecas = inicia_jogo(n_jogadores, pecas)
    monte = dicionario_pecas['monte']

    # Cria ordem de jogadas aleatório
    ordem_jogadores = embaralha_jogaderes(n_jogadores)

    # loop q se repete até um jogador não ter peças
    j = True
    while j:

        for i in ordem_jogadores:
            
            # controla vez do computador ou jogador
            if i == 0:
                # Mostra peças ao jogador 0
                print('Você está com {} peças em mãos.'.format(len(dicionario_pecas['jogadores'][0])))
                print(cor_pecas(dicionario_pecas['jogadores'][0]))

                # Define e printa a mesa inicial 
                print()
                print('MESA: {}'.format(cor_mesa(dicionario_pecas['mesa'])))


                h = True 
                while h:

                    possibilidade = posicoes_possiveis(dicionario_pecas['mesa'], dicionario_pecas['jogadores'][0]) 

                    while (possibilidade == []) and (monte != []):

                        print()
                        print('Não há jogadas possíveis. Compre do monte')
                        dicionario_pecas['jogadores'][0] += [monte[0]]
                        del monte[0]
                        print()
                        print('Você está com {} peças em mãos.'.format(len(dicionario_pecas['jogadores'][0])))
                        print(cor_pecas(dicionario_pecas['jogadores'][0]))
                        print()
                        print('MESA: {}'.format(cor_mesa(dicionario_pecas['mesa'])))
                        print()
                        
                        possibilidade = posicoes_possiveis(dicionario_pecas['mesa'], dicionario_pecas['jogadores'][0])

                    if possibilidade == [] and monte == []:
                        
                        print('Você está com {} peças em mãos.'.format(len(dicionario_pecas['jogadores'][0])))
                        print(dicionario_pecas['jogadores'][0])
                        print()
                        print('Não há peças possíveis e não há peças disponíveis no monte. Aguarde a próxima rodada.')
                        h = False

                    if possibilidade != []: 

                        jogada = int(input('Escolha a peça: '))
                        jogada -= 1
                        print()

                        while jogada not in possibilidade:
                            print('Jogada inválida.')
                            jogada = int(input('Escolha outra peça: '))
                            jogada -= 1
                            print()

                        if jogada in possibilidade:
                    
                            dicionario_pecas['mesa'] = adiciona_na_mesa(dicionario_pecas['jogadores'][0][jogada], dicionario_pecas['mesa'])
                            del(dicionario_pecas['jogadores'][0][jogada])

                        verificador = verifica_ganhador(dicionario_pecas['jogadores'])

                        if verificador == 0:
                            j = False
                            break

                        h = False
                    


            else:

                print('Jogador {} está com {} peças em mãos.'.format(i, len(dicionario_pecas['jogadores'][i])))

                h = True 
                while h:

                    jogada_PC = posicoes_possiveis(dicionario_pecas['mesa'], dicionario_pecas['jogadores'][i])

                    while (jogada_PC == []) and (monte != []):

                        dicionario_pecas['jogadores'][i] += [monte[0]]
                        del monte[0]

                        print('Jogador {} comprou do monte.'.format(i))
                        print('Jogador {} está com {} peças em mãos.'.format(i, len(dicionario_pecas['jogadores'][i])))

                        jogada_PC = posicoes_possiveis(dicionario_pecas['mesa'], dicionario_pecas['jogadores'][i])

                    if jogada_PC == [] and monte == []:
                        print('Jogador {} não tinha peças possíveis e o monte está vazio. Passou a vez.\n'.format(i))
                        
                        h = False

                    if jogada_PC != []:
                        dicionario_pecas['mesa'] = adiciona_na_mesa(dicionario_pecas['jogadores'][i][jogada_PC[0]], dicionario_pecas['mesa'])
                        print('Jogador {} colocou a peça {} \n'.format(i, cor_peca(dicionario_pecas['jogadores'][i][jogada_PC[0]])))
                        del(dicionario_pecas['jogadores'][i][jogada_PC[0]])
                    
                    verificador = verifica_ganhador(dicionario_pecas['jogadores'])

                    if verificador == i:
                        j = False
                        break

                    h = False 

    if verificador == 0: 
        print('Parabéns! Você ganhou!')
    else: 
        print('Que pena, jogador {} ganhou'.format(verificador))

    new_game = input('Deseja iniciar novo jogo? (sim ou não) ')
    print()
    if new_game == 'sim':
        start = True
    else: 
        start = False 
