lstNumeros = list()

intLimite  = 100

# Gerando uma lista de números de 0 até intLimite - 1 
for intValor in range(intLimite):
   lstNumeros.append(intValor)

# Imprimindo os números da lista informando se são pares ou ímpares
for intNumero in lstNumeros:
   if intNumero % 2 == 0:
      print(f'{intNumero} é par')
   else:
      print(f'{intNumero} é ímpar')
