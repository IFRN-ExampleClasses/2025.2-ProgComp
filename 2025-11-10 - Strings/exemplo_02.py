'''
    Exemplo 02: Imprimindo cada letra de um texto em uma linha diferente
'''

strTexto = input('Digite algo: ')

# Usando FOR
print('-'*80)
print('Usando FOR')
for letra in strTexto:
    print(letra)


# Usando WHILE
print('-'*80)
print('Usando WHILE')
intPos = 0
while intPos < len(strTexto):
   print(strTexto[intPos])
   intPos += 1