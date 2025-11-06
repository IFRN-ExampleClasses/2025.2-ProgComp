'''
   Faça um programa que solicite ao usuário um número inteiro e
   informe se ele é primo ou não.
'''
import sys

try:
   intNumero = int(input('Digite um número inteiro: '))
except ValueError:
   sys.exit('ERRO: Informe um número inteiro válido...')
except KeyboardInterrupt:
   sys.exit('AVISO: Programa interrompido pelo usuário...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   # Números primos são maiores que 1
   if intNumero < 2:
      sys.exit(f'O número {intNumero} não é primo.')

   # Conta a quantidade de divisores
   intQtDivisores = 1

   # Verifica os divisores de 2 até o número informado
   for intDivisor in range(2, intNumero + 1):
      if intNumero % intDivisor == 0:
         intQtDivisores += 1
      if intQtDivisores > 2: break

   # Se tiver 2 divisores, é primo
   if intQtDivisores == 2:
      print(f'O número {intNumero} é primo.')
   else:
      print(f'O número {intNumero} não é primo.')
