'''
   Exemplo 03: Imprimindo cada palavra de um texto em uma linha diferente
'''

strTexto = input('Digite um texto qualquer: ')

for letra in strTexto:
   if letra != ' ':
       print(letra, end='')   # end='' para não pular linha
   else:
       print('')              # end='\n' por padrão
