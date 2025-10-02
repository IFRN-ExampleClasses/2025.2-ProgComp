'''
   Fazer um programa que solicite ao usuário dois números. Esses números
   correspondem as coordenadas x e y de um ponto em um plano cartesiano.

   Após receber os números, o programa deve informar em qual quadrante
   o ponto se encontra. 

   Lembrete: O plano cartesiano é dividido em quatro quadrantes:
   - Quadrante 1: Ambas as coordenadas (x e y) são positivas;
   - Quadrante 2: A coordenada x é negativa e a coordenada y é positiva;
   - Quadrante 3: Ambas as coordenadas (x e y) são negativas;
   - Quadrante 4: A coordenada x é positiva e a coordenada y é negativa;
   - Se o ponto for a origem (0,0), o programa deve informar que o ponto está 
     na origem.
   - Se o ponto estiver sobre um dos eixos (x ou y), o programa deve informar
     que o ponto está sobre o eixo correspondente:
       - Sobre o eixo x: y = 0
       - Sobre o eixo y: x = 0
'''

fltCoordX = float(input('Digite a coordenada X: '))
fltCoordY = float(input('Digite a coordenada Y: '))

if (fltCoordX > 0) and (fltCoordY > 0): 		# if (fltCoordX and fltCoordY > 0):
   print('O ponto está no 1º Quadrante.')
elif (fltCoordX < 0) and (fltCoordY > 0):
   print('O ponto está no 2º Quadrante.') 
elif (fltCoordX < 0) and (fltCoordY < 0):		# if (fltCoordX and fltCoordY < 0):
   print('O ponto está no 3º Quadrante.')
elif (fltCoordX > 0) and (fltCoordY < 0):
   print('O ponto está no 4º Quadrante.')
elif (fltCoordX == 0) and (fltCoordY == 0):	# if (fltCoordX and fltCoordY = 0):
   print('O ponto está na origem (0,0).')
elif (fltCoordY == 0):
   print('O ponto está sobre o eixo X.')
else:
   print('O ponto está sobre o eixo Y.')

