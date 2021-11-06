RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
MISTERIO1  = "\033[1;35m"
YELLOW  = "\033[1;33m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def colorir(pecas): 

   pecas2 = []

   peca2 = []

   cor = 0

   for peca in pecas: 
      for n in peca: 

         if n == 0: 
            cor = RED + str(n) + RESET
            peca2.append(cor)

            print(n)

      pecas2.append(peca2)

   return pecas2
            

print(colorir([[0,0]]))

def colorir2(pecas):
    pecas = str(pecas)

    for p in pecas: 

      if p == '[':
         p = p

      if p == ' ':
         p = p

      if p == ',':
         p = p

      if p == ']':
         p = p

      if p == '0':
         p = RED + p + RESET

      if p == '1':
         p = BLUE + p + RESET

      if p == '2':
         p = GREEN + p + RESET

      if p == '3':
         p = CYAN + p + RESET

      if p == '4':
         p = YELLOW + p + RESET

      if p == '5':
         p = MISTERIO1 + p + RESET

      if p == '6':
         p = p

      return pecas 

print(colorir2([[0,0], [0,1], [0,2]]))





