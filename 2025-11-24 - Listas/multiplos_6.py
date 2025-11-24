'''
   Gerando uma lista com os múltiplos de 6 entre 1 e um número n informado pelo usuário. 
'''
import sys

try:
   intLimite = int(input('Digite um número inteiro positivo: '))
except ValueError:
   sys.exit('Valor inválido!')
except Exception as e:
   sys.exit(f'Erro inesperado: {e}')
else:
   if intLimite <= 0:
      sys.exit('O número deve ser positivo!') 

   listaMultiplos6 = list()

   for numero in range(1, intLimite + 1):
      if numero % 6 == 0:
         listaMultiplos6.append(numero)

   print(f'Lista dos múltiplos de 6 entre 1 e {intLimite}: {listaMultiplos6}')