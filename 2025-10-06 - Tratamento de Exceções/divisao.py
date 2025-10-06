'''
	Você deve criar um programa que calcule o quociente entre dois números 
   inteiros fornecidos pelo usuário. Durante o processo, é necessário 
   tratar as seguintes exceções:

		- Caso o segundo número seja zero, o programa deve exibir uma mensagem 
		  informando que a divisão por zero não é permitida.

		- Caso o usuário insira um valor que não seja um número inteiro, o 
        programa deve exibir uma mensagem solicitando que o usuário insira 
        apenas números inteiros.

	Instruções:

		- Solicite ao usuário para inserir o primeiro número inteiro.

		- Solicite ao usuário para inserir o segundo número inteiro.

		- Calcule o quociente entre os dois números, tratando as exceções 
        descritas acima.
'''
import sys

try:
   intDividendo = int(input('Informe o Dividendo: '))
   intDivisor   = int(input('Informe o Divisor..: '))
   quociente    = intDividendo / intDivisor
except ZeroDivisionError:
   sys.exit('ERRO: Divisão por Zero não é permitida...')
except ValueError:
   sys.exit('ERRO: Informe apenas números inteiros...')
except Exception as strErro:
   sys.exit(f'EXCEÇÃO: {sys.exc_info()[0]} -> {strErro}')
else:
   print(f'{intDividendo} / {intDivisor} = {quociente:.2f}')
