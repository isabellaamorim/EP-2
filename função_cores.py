cores = {0: "\033[1;31m" , 
1: "\033[0;32m",
2: "\033[1;33m",
3: "\033[1;34m", 
4: "\033[1;35m", 
5: "\033[1;36m",
6: "\033[1;30m"}

reset = "\033[0;0m"

def cor_peca(p):

   cor1 = cores[p[0]] + f'{p[0]}' + reset 
   cor2 = cores[p[1]] + f'{p[1]}' + reset

   peca = '[' + cor1 + ' ' + '|' + ' ' + cor2 + ']'
   return peca

def cor_pecas(pecas): 

   pecas1 = ''

   for p in pecas:

      cor1 = cores[p[0]] + f'{p[0]}' + reset 
      cor2 = cores[p[1]] + f'{p[1]}' + reset

      peca = '[' + cor1 + '|' + cor2 + ']'

      pecas1 += ' ' + peca 

   return pecas1

def cor_mesa(pecas): 

   if len(pecas) == 0: 
      return ''

   mesa = ''

   for p in pecas:

      cor1 = cores[p[0]] + f'{p[0]}' + reset 
      cor2 = cores[p[1]] + f'{p[1]}' + reset

      peca = '[' + cor1 + '|' + cor2 + ']'

      mesa +=  peca 

   return mesa

print(cor_mesa([[0,1], [2,3], [4,5], [6,0]]))



   

