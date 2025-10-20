'''
   Desenvolva um código em Python que solicite ao usuário que informe os 
   comprimentos dos três lados de um triângulo. 
   
   Em seguida, verifique se esses comprimentos podem formar um triângulo. 
   Caso afirmativo, calcule e informe os valores dos ângulos do triângulo e 
   classifique-o quanto aos lados e aos ângulos.

   Instruções:
      - Peça ao usuário para inserir os comprimentos dos três lados do triângulo;
      - Verifique se os comprimentos fornecidos podem formar um triângulo. 
        Caso contrário, informe que não é possível formar um triângulo com esses lados;
      - Se for possível formar um triângulo, calcule os três ângulos do triângulo;
      - Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) 
        e aos ângulos (agudo, obtuso ou retângulo);
      - Exiba a classificação do triângulo quanto aos lados e aos ângulos.

   Observações:
      - Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, 
        é necessário verificar a seguinte condição: A soma de quaisquer dois lados de 
        um triângulo deve ser sempre maior que o terceiro lado;
      - Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo;
      - Para classificar quanto aos lados, verifique se os três lados são iguais 
        (equilátero), se dois lados são iguais (isósceles) ou se todos os lados são 
        diferentes (escaleno);
      - Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 
        90 graus (obtuso), se um dos ângulos é igual a 90 graus (retângulo) 
        ou se todos os ângulos são menores que 90 graus (agudo);
      - Considere que os ângulos são expressos em graus.

   Dica: Utilize a biblioteca math.
   https://docs.python.org/3/library/math.html
'''
import math, sys

try:
  # Informa os lados do triângulo
  fltLadoA = float(input('Informe o comprimento do lado A: '))
  fltLadoB = float(input('Informe o comprimento do lado B: '))
  fltLadoC = float(input('Informe o comprimento do lado C: '))

except ValueError:
  sys.exit('ERRO: Valor inválido. Informe um número real.')

except Exception as e:
  sys.exit(f'ERRO INESPERADO: {e}')

else:
  # ----------------------------------------------------------------------
  # Verificando se os lados são positivos
  if fltLadoA <= 0 or fltLadoB <= 0 or fltLadoC <= 0:
    sys.exit('ERRO: Os lados do triângulo devem ser números positivos.')

  # ----------------------------------------------------------------------
  # Verificando se os lados podem formar um triângulo
  if (fltLadoA + fltLadoB <= fltLadoC) or (fltLadoA + fltLadoC <= fltLadoB) or (fltLadoB + fltLadoC <= fltLadoA):
    sys.exit('ERRO: Os lados informados não podem formar um triângulo.') 

  # ----------------------------------------------------------------------
  # Calculando os ângulos do triângulo usando a Lei dos Cossenos e a função
  # arco-cosseno (math.acos) da biblioteca math para obter os ângulos em radianos.
  # Em seguida, converte os ângulos de radianos para graus usando a função 
  # math.degrees() e round() para evitar problemas de precisão com números 
  # de ponto flutuante.  

  # Calculando o cosseno do ângulo A e do ângulo B
  # cos(A) = (b² + c² - a²) / 2bc
  fltCossenoA = (fltLadoB**2 + fltLadoC**2 - fltLadoA**2) / (2 * fltLadoB * fltLadoC)
  # cos(B) = (a² + c² - b²) / 2ac
  fltCossenoB = (fltLadoA**2 + fltLadoC**2 - fltLadoB**2) / (2 * fltLadoA * fltLadoC)

  # Aplicando a função arco-cosseno para obter o ângulo A e o ângulo B em radianos
  fltAnguloA = math.acos(fltCossenoA)
  fltAnguloB = math.acos(fltCossenoB)

  # Convertendo os ângulos para graus e usando round() para evitar problemas
  # de precisão com números de ponto flutuante
  fltAnguloA = round(math.degrees(fltAnguloA), 5)
  fltAnguloB = round(math.degrees(fltAnguloB), 5)
  
  # Calculando o ângulo C
  fltAnguloC = 180 - fltAnguloA - fltAnguloB

  # ----------------------------------------------------------------------
  # Classificando o triângulo quanto aos lados
  if (fltLadoA == fltLadoB) and (fltLadoB == fltLadoC):
    strClassificacaoLados = 'Equilátero'
  elif (fltLadoA == fltLadoB) or (fltLadoA == fltLadoC) or (fltLadoB == fltLadoC):
    strClassificacaoLados = 'Isósceles'
  else:
    strClassificacaoLados = 'Escaleno'

  # ----------------------------------------------------------------------
  # Classificando o triângulo quanto aos ângulos
  if (fltAnguloA == 90) or (fltAnguloB == 90) or (fltAnguloC == 90):
    strClassificacaoAngulos = 'Retângulo'
  elif (fltAnguloA > 90) or (fltAnguloB > 90) or (fltAnguloC > 90):
    strClassificacaoAngulos = 'Obtusângulo'
  else:
    strClassificacaoAngulos = 'Acutângulo'

  # ----------------------------------------------------------------------
  # Exibindo os resultados
  print('------------------------------------------------------')
  print(f'\nÂngulos do triângulo:')
  print(f'Ângulo A ...........: {fltAnguloA:.5f}°')
  print(f'Ângulo B ...........: {fltAnguloB:.5f}°')
  print(f'Ângulo C ...........: {fltAnguloC:.5f}°')

  print('------------------------------------------------------')
  print(f'\nClassificação do triângulo:')
  print(f'Quanto aos lados ...: {strClassificacaoLados}')
  print(f'Quanto aos ângulos .: {strClassificacaoAngulos}\n')
