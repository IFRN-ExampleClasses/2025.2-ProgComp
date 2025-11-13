'''
   Exemplo 02: Programa para contar quantas palavras existem em uma frase
   fornecida pelo usuário.
'''
strFrase = input('Digite uma frase: ')

'''
intContador = 0

for strCaractere in strFrase:
    if strCaractere.isspace():
        intContador += 1
'''

listaPalavras = strFrase.split()
intContador = len(listaPalavras)

print(f'Número de palavras: {intContador}')