lstNumeros = list()

intLimite  = 100

# Gerando uma lista de números de 0 até intLimite - 1 
'''
for intValor in range(intLimite):
   lstNumeros.append(intValor)
'''
intValor = 0
while intValor < intLimite:
   lstNumeros.append(intValor)
   intValor += 1
   
# Imprimindo os números da lista informando se são pares ou ímpares
'''
for intNumero in lstNumeros:
   if intNumero % 2 == 0:
      print(f'{intNumero} é par')
   else:
      print(f'{intNumero} é ímpar')
'''
intPosicao = 0
while intPosicao < len(lstNumeros):
   if lstNumeros[intPosicao] % 2 == 0:
      print(f'{lstNumeros[intPosicao]} é par')
   else:
      print(f'{lstNumeros[intPosicao]} é ímpar')
   intPosicao += 1