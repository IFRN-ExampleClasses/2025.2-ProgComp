'''
   Contando de 1 a 10 e exibindo se o número é par ou ímpar
'''

# Definindo a variável de controle
intNumero= 1

# Iniciando o loop while: 
# enquanto intNumero for menor ou igual a 10
while intNumero <= 10:

   # Verifica se o número é par ou ímpar
   if (intNumero % 2) == 0:
      print(f'{intNumero} é Par')
   else:
      print(f'{intNumero} é Ímpar')

   # Incrementa a variável de controle
   intNumero += 1