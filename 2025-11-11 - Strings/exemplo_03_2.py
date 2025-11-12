'''
   Exemplo 03: Imprimindo cada palavra de um texto em uma linha diferente
'''

strTexto = input('Digite um texto qualquer: ')

'''
for letra in strTexto:
   if letra != ' ':
       print(letra, end='')   # end='' para não pular linha
   else:
       print('')              # end='\n' por padrão
'''

for letra in strTexto:
   # Usando expressão condicional direto no parâmetro end (ternário)
   print(letra, end='' if letra != ' ' else '\n')
