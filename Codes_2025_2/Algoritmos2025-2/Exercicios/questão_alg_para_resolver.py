#N = 7, o output é uma letra embaixo da outra
#######   #     #   ######  
   #      ##   ##   #     # 
   #      # # # #   #     # 
   #      #  #  #   ######  
   #      #     #   #       
#  #      #     #   #       
 ###      #     #   #

#start stop step

n = int(input("Digite o Tamanho"))
meio = n // 2
for i in range (n):
   caracteres = [' '] * n
   if i == 0:
      caracteres = ['#']  * n
   elif i != n - 1 and i != n - 2:
      caracteres[meio] = '#'
   elif i == n - 2:
      caracteres[n - n + 1 :meio + 1: 2] = '#' * 2
   elif i == n - 1:
      caracteres[meio -1:meio: 1] = '#' * 3
      
   print("".join(caracteres))