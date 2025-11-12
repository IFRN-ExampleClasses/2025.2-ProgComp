'''
   Exemplo 04: Inversão de uma palavra

   Utilizando [::-1] para inverter uma string e verificar se é um palíndromo.
'''

import sys

strTexto = input('Digite uma palavra qualquer: ')

if ' ' in strTexto:
   sys.exit('ERRO: A entrada deve ser uma única palavra, sem espaços.')

# Invertendo a string usando slicing
strTextoInvertido = strTexto[::-1]

print(f'A palavra digitada foi.: {strTexto}')
print(f'A palavra invertida é..: {strTextoInvertido}')

if strTexto.lower() == strTextoInvertido.lower():
   print('A palavra digitada é um palíndromo!')
else:
   print('A palavra digitada não é um palíndromo.')

