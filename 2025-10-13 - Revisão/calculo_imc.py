'''
   Desenvolva um programa que calcula o IMC de uma pessoa. 
   
   O programa deve pedir o peso em quilogramas (ex: 70.5) e a 
   altura em metros (ex: 1.75). 
   
   A fórmula do IMC é: peso / (altura * altura). 
   
   Após calcular o IMC, o programa deve exibir o valor e a 
   classificação correspondente, de acordo com a tabela:

      - Abaixo de 18.5: Abaixo do peso
      - 18.5 a 24.9: Peso ideal
      - 25.0 a 29.9: Sobrepeso
      - 30.0 a 34.9: Obesidade Grau I
      - 35.0 a 39.9: Obesidade Grau II
      - 40.0 ou mais: Obesidade Grau III

   O programa deve tratar entradas inválidas (não numéricas) e 
   também verificar se a altura informada é maior que zero para evitar 
   um erro de divisão.      
'''
import sys

# Entrada de dados com tratamento de erro
try:
   fltPeso   = float(input('Informe o seu peso em quilogramas (ex: 70.5): '))
   fltAltura = float(input('Informe a sua altura em metros (ex: 1.75)...: '))
# Tratamento de erro para valores não numéricos
except ValueError:
   sys.exit('ERRO: Você deve digitar um valor numérico.')
# Tratamento de erro para outros tipos de erro
except Exception as strErro:
   sys.exit(f'ERRO: {strErro}')
# Cálculo do IMC caso tenha passado pelas validações
else:
   # Verifica se a altura é menor ou igual a zero
   if fltAltura <= 0:
      sys.exit('ERRO: A altura deve ser maior que zero.')

   # Verifica se o peso é menor ou igual a zero
   if fltPeso <= 0:
      sys.exit('ERRO: O peso deve ser maior que zero.')

   # Cálculo do IMC
   fltIMC = fltPeso / (fltAltura * fltAltura)

   print(f'Seu IMC é {fltIMC:.1f}.')

   # Classificação do IMC
   if fltIMC < 18.5:
      print('Classificação: Abaixo do peso.')
   elif fltIMC < 25.0:
      print('Classificação: Peso ideal.')
   elif fltIMC < 30.0:
      print('Classificação: Sobrepeso.')
   elif fltIMC < 35.0:
      print('Classificação: Obesidade Grau I.')
   elif fltIMC < 40.0:
      print('Classificação: Obesidade Grau II.')
   else:
      print('Classificação: Obesidade Grau III.')