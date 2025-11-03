'''
   Reescreva o programa a seguir usando o laço FOR.
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

   ''' Versão com WHILE '''
   '''
   intAuxiliar = intNumero
   intFatorial = 1

   while intAuxiliar > 1:
      intFatorial *= intAuxiliar
      intAuxiliar -= 1
   '''

   ''' Versão com FOR '''
   intFatorial = 1
   for intAuxiliar in range(intNumero, 1, -1):
      intFatorial *= intAuxiliar

   print(f'{intNumero}! = {intFatorial}')