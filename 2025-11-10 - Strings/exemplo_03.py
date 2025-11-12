'''
    Exemplo 03: Imprimindo do início do texto até a posição atual em cada linha
'''

strTexto = input('Digite algo: ')

# Usando FOR
print('-'*80)
print('Usando FOR')
strAux = ''
for letra in strTexto:
    strAux += letra
    print(strAux)


# Usando WHILE
print('-'*80)
print('Usando WHILE')
intPos = 1
while intPos <= len(strTexto):
   print(strTexto[:intPos])
   intPos += 1