'''
	Crie um programa em Python que calcule as raízes de uma equação do 2º grau.
	
	O programa deve:
	
		- Ler os valores de a, b e c como entrada;
		
		- Verificar se o valor de a é zero. Caso seja, a equação não será do 
		  2º grau e o programa deve informar o usuário sobre isso e encerrar;
		  
		- Calcular o discriminante(delta) e, com base no valor de delta:
			
			- delta > 0 : a equação possui duas raízes reais distintas. 
			  O programa deve calcular e exibir ambas as raízes;
			  
			- delta = 0 : a equação possui uma única raiz real. 
			  O programa deve calcular e exibir a raiz única;
			  
			- delta < 0 : a equação não possui raízes reais. 
			  O programa deve informar ao usuário que não existem raízes reais
			  
'''
import sys

a = float(input('Digite o valor de a: '))

if a == 0:
   sys.exit('O valor de a não pode ser zero. A equação não é do 2º grau.')

b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b**2 - 4*a*c

if delta > 0:
   raiz1 = (-b + delta**0.5) / (2*a)
   raiz2 = (-b - delta**0.5) / (2*a)
   print(f'A equação possui duas raízes reais distintas: {raiz1} e {raiz2}')
elif delta == 0:
   raiz = -b / (2*a)
   print(f'A equação possui uma única raiz real: {raiz}')
else:
   print('A equação não possui raízes reais.')
