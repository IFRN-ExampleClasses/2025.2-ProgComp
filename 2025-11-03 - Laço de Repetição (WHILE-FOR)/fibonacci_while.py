'''
   Programa que solicita um número inteiro ao usuário e exiba os n
   primeiros elementos da Série de Fibonacci (usando WHILE).

   Exemplo: n = 10

   Saída: 
      1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''
import sys

try:
   intN = int(input('Digite um número inteiro: '))
except ValueError:
   sys.exit('ERRO: Por favor, digite um número inteiro...')
except KeyboardInterrupt:
   sys.exit('\nAVISO: CTRL+C pressionado pelo usuário...')
except Exception as e:
   sys.exit(f'ERRO: {e}...')
else:
   if intN <= 1:
      sys.exit('ERRO: Por favor, digite um número maior que 1...')

   intAnterior, intAtual = 0, 1

   intContador = 1
   while intContador <= intN:
      print(f'{intAtual},', end=' ')
      intAnterior, intAtual = intAtual, intAnterior + intAtual
      intContador += 1
