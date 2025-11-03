'''
   Reescreva o programa a seguir usando o laço FOR.
'''

intMultiplicador = 6

''' Versão com WHILE '''
'''
intMultiplicando = 1
# Definição do laço de repetição
# Exibe a tabuada do 6 enquanto o multiplicando for menor ou igual a 10
while intMultiplicando <= 10:
   # Cálculo do produto
   intProduto = intMultiplicador * intMultiplicando
   # Exibição do resultado
   print(f'{intMultiplicador} x {intMultiplicando} = {intProduto}')
   # Incremento do multiplicando
   intMultiplicando += 1
'''

''' Versão com FOR '''
for intMultiplicando in range(1, 11):
   # Cálculo do produto
   intProduto = intMultiplicador * intMultiplicando
   # Exibição do resultado
   print(f'{intMultiplicador} x {intMultiplicando} = {intProduto}')