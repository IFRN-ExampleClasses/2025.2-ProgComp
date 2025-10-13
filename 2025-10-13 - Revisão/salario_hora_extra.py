'''
   Crie um programa que calcula o salário semanal de um funcionário.
   
   O programa deve solicitar o número de horas trabalhadas na semana e o 
   valor que ele recebe por hora. 
   
   A jornada de trabalho padrão é de 40 horas semanais. Horas trabalhadas 
   acima de 40 devem ser pagas com um adicional de 50% (o valor da hora 
   extra é 1.5 vezes o valor da hora normal). 
   
   O programa deve exibir o salário total. 
   
   Garanta que o programa trate o caso de o usuário digitar valores não 
   numéricos.
'''
import sys

# Entrada de dados com tratamento de erro
try:
   intHoras     =   int(input('Informe o número de horas trabalhadas na semana: '))
   fltValorHora = float(input('Informe o valor que você recebe por hora.......: '))
# Tratamento de erro para valores não numéricos
except ValueError:
   sys.exit('ERRO: Você deve digitar um valor numérico.')
# Tratamento de erro para outros tipos de erro
except Exception as strErro:
   sys.exit(f'ERRO: {strErro}')
# Cálculo do salário caso tenha passado pelas validações 
else:
   # Verifica se a quantidade de horas trabalhadas é negativa 
   if intHoras < 0:
      sys.exit('ERRO: O número de horas trabalhadas não pode ser negativo.')

   # Verifica se o valor da hora é negativo
   if fltValorHora < 0:
      sys.exit('ERRO: O valor da hora não pode ser negativo.')

   # Verifica se houve horas extras
   intHorasExtras = 0
   if intHoras > 40:
      intHorasExtras = intHoras - 40
      intHoras = 40

   # Cálculo do salário
   fltSalario = (intHoras * fltValorHora) + (intHorasExtras * fltValorHora * 1.5)

   # Exibição do resultado
   print(f'Você trabalhou {intHoras + intHorasExtras} horas nesta semana.')
   print(f'O valor da sua hora é R$ {fltValorHora:.2f}.')
   print(f'Seu salário semanal é de R$ {fltSalario:.2f}')
