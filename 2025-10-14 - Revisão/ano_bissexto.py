'''
   Escreva um programa que pede ao usuário para inserir um ano e 
   determina se ele é bissexto ou não. 
   
   Um ano é bissexto se atender a uma das seguintes regras:

      - É divisível por 4, mas não é divisível por 100.

      - É divisível por 400.

      (Por exemplo, 2000 e 2400 são bissextos; 1800, 1900 e 2100 não são). 
      
   O programa deve exibir "O ano [ano] é bissexto." ou 
   "O ano [ano] não é bissexto.". 
   
   Use try...except para validar a entrada.
'''
import sys

# Entrada de dados com tratamento de erro
try:
   intAno = int(input('Informe um ano (ex: 2024): '))
# Tratamento de erro para valores não numéricos
except ValueError:
   sys.exit('ERRO: Você deve digitar um valor numérico inteiro.')
# Tratamento de erro para outros tipos de erro
except Exception as strErro:
   sys.exit(f'ERRO: {strErro}')
# Verificação se o ano é bissexto caso tenha passado pelas validações
else:
   # Verifica se o ano é menor ou igual a zero
   if intAno <= 0:
      sys.exit('ERRO: O ano deve ser maior que zero.')

   # Verifica se o ano é bissexto
   if (intAno % 4 == 0 and intAno % 100 != 0) or (intAno % 400 == 0):
      print(f'O ano {intAno} é bissexto.')
   else:
      print(f'O ano {intAno} não é bissexto.')  

