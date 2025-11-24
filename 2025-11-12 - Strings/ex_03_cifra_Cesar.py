'''
   Exemplo 03: Programa para aplicar a Cifra de Cesar em uma mensagem 
   fornecida pelo usuário.

   A mensagem só pode conter letras maiúsculas (sem acentos), letras 
   minúsculas (sem acentos) e espaços.
'''
import sys

try:
   strMensagem     = input('Digite a mensagem: ')
   intDeslocamento = int(input('Digite o deslocamento (ex: 3): '))
   strCifraCesar   = ''
except ValueError:
   sys.exit('ERRO: Informe Valores inteiros...')
except Exception as strErro:
   sys.exit(f'ERRO: {strErro}')
else:
   if not all(c.isalpha() or c.isspace() for c in strMensagem):
      sys.exit('ERRO: Use apenas letras de A-Z/a-z e espaços em branco...')

   if intDeslocamento < 1:
      sys.exit('ERRO: Informe um deslocamento positivo...')

   for strLetra in strMensagem:
      if strLetra.isspace():
         strLetraCifra = strLetra
      elif strLetra.isupper():
         intBase       = ord('A')
         strLetraCifra = chr((ord(strLetra) - intBase + intDeslocamento) % 26 + intBase)
      else:
         intBase       = ord('a')
         strLetraCifra = chr((ord(strLetra) - intBase + intDeslocamento) % 26 + intBase)
      
      strCifraCesar += strLetraCifra

   print(f'Mensagem Cifrada: {strCifraCesar}')