'''
   Faça um programa que solicite ao usuário um número inteiro e 
   informe em quantas interações ele converge para a constante de 
   Kaprekar (6174). Lembre-se que o número não deve ter 4 dígitos 
   iguais. Caso o número não atenda a essa condição, informe
   que ele é inválido.

   O que é a constante de Kaprekar?
   A constante de Kaprekar é o número 6174, que é alcançado através
   de um processo repetitivo de manipulação de números de 4 dígitos.

   Como funciona o processo de Kaprekar:
   1. Pegue qualquer número de 4 dígitos com pelo menos dois dígitos diferentes.
   2. Ordene os dígitos em ordem crescente e decrescente para formar dois números diferentes.
   3. Subtraia o menor número do maior número.
   4. Repita o processo com o resultado até chegar a 6174.

   Exemplo:
   - Comece com o número 3524.
   - Ordene os dígitos: 5432 (decrescente) e 2345 (crescente).
     1ª iteração: 5432 - 2345 = 3087
   - Repita o processo:
     2ª iteração: 8730 - 0378 = 8352
     3ª iteração: 8532 - 2358 = 6174
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
   # Verifica se o número está dentro do intervalo válido
   if intNumero < 1000 or intNumero > 9999:
      sys.exit(f'ERRO: O número {intNumero} é inválido. Deve ter exatamente 4 dígitos.')

   # Verifica se todos os dígitos são iguais
   '''
   strNumero     = int(intNumero)
   strPrimDigito = str(strNumero)[0]
   if strNumero.count(strPrimDigito) == 4:
      sys.exit(f'ERRO: O número {intNumero} é inválido. Deve conter pelo menos dois dígitos diferentes.')
   '''
   if str(intNumero).count(str(intNumero)[0]) == 4:
      sys.exit(f'ERRO: O número {intNumero} é inválido. Deve conter pelo menos dois dígitos diferentes.')

   # ------------------------------------------------------------
   # Inicializa o contador de iterações
   intIteracoes = 1
  
   while intNumero != 6174:
      strNumero = str(intNumero).zfill(4)
  
      strCrescente   = ''.join(sorted(strNumero))
      strDecrescente = ''.join(sorted(strNumero, reverse=True))

      intMaior = int(strDecrescente)
      intMenor = int(strCrescente)
  
      intNumero = intMaior - intMenor

      print(f'{intIteracoes}ª iteração: {intMaior:04d} - {intMenor:04d} = {intNumero:04d}')

      intIteracoes += 1

   print(f'O número converge para a constante de Kaprekar (6174) em {intIteracoes} iterações.')
