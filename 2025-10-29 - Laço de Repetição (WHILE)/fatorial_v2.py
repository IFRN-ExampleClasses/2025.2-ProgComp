'''
   Fazer um programa que solicite um número inteiro e calcule seu fatorial
'''
import sys

try:
   intNumero = int(input('Informe um valor inteiro: '))
except ValueError:
   sys.exit('ERRO: O valor informado deve ser inteiro...')
except:
   sys.exit(f'ERRO: {sys.exc_info()}')
else:
   if intNumero < 0:
      sys.exit('ERRO: Não existe fatorial de número negativo...')

   if intNumero == 0 or intNumero == 1:
      sys.exit(f'{intNumero}! = 1')

   print(f'{intNumero}! = {intNumero}', end='')

   intFatorial = 1

   while intNumero > 1:
      intFatorial *= intNumero
      intNumero -= 1
      print(f' x {intNumero}', end='')

   print(f' x 1 = {intFatorial}')
   

   