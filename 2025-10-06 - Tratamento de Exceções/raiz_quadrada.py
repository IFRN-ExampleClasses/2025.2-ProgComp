'''
   criar um programa que permita ao usuário calcular a raiz quadrada de um 
   número inteiro. Entretanto, o programa deve cumprir os seguintes requisitos:

   - Se o usuário inserir um número negativo, o programa deve lançar uma 
     exceção personalizada chamada "FloatingPointError" com uma mensagem
     apropriada;

   - Se o usuário inserir um valor que não seja um número inteiro, o programa
     deve capturar a exceção "ValueError" e exibir uma mensagem informando
     que o valor inserido é inválido;

   - Caso  o número for positivo ou zero, o programa deve calcular e exibir a 
     raiz quadrada do número com duas casas decimais.

   Instruções:
      - Solicite ao usuário para inserir um número inteiro.

      - Implemente o tratamento de exceções conforme os requisitos acima.
      
      - Calcule e exiba a raiz quadrada do número, se aplicável.
'''
import sys

try:
   intValor = int(input('Informe um valor inteiro: '))
    
   # Criando a exceção 'NegativeSquareRoot' para números negativos
   if intValor < 0:
       raise Exception('NegativeSquareRoot')
   
   intRaizQuadrada = intValor ** 0.5
except ValueError:
   sys.exit('ERRO: Por favor, insira apenas números inteiros.')
except Exception as strErro:
   if str(strErro) == 'NegativeSquareRoot':
       sys.exit('ERRO: Não há Raiz Real para números negativos...')
   else:
       sys.exit(f'ERRO: {strErro}')
else:
   print(f'A raiz quadrada de {intValor} é {intRaizQuadrada:.2f}')
