'''
   Exemplo 01: Programa para contar quantas vogais existem em uma string 
   fornecida pelo usuário.
'''
strTexto    = input('Digite algo: ')

strVogais   = 'aeiouáéíóúàèìòùâêîôûãõäëïöü'

intContador = 0

for strLetra in strTexto.lower():
    if strLetra in strVogais:
        intContador += 1

print(f'Número de vogais = {intContador}')