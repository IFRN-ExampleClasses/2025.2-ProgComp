'''
   Faça um programa que solicite ao usuário um número inteiro e
   informe se ele é um número triangular ou não.

   Um número triangular é um número que pode ser representado na forma 
   de um triângulo equilátero.

   Os primeiros números triangulares são: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
'''
import sys, math

try:
   intNumero = int(input('Digite um número inteiro: '))
except ValueError:
   sys.exit('ERRO: Informe um número inteiro válido...')
except KeyboardInterrupt:
   sys.exit('AVISO: Programa interrompido pelo usuário...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   # Números triangulares são positivos
   if intNumero < 1:
      sys.exit(f'O número {intNumero} não é triangular.')

   # Verifica se o número é triangular
   # https://pt.wikipedia.org/wiki/N%C3%BAmero_triangular

   # Aplica a fórmula inversa: n = (-1 + sqrt(1 + 8*num)) / 2
   intPosicao = ( -1 + math.isqrt(1 + 8 * intNumero) ) / 2

   if intPosicao.is_integer() and intPosicao > 1:
      print(f'O número {intNumero} é triangular.')
   else:
      print(f'O número {intNumero} não é triangular.')