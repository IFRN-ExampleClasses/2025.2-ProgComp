'''
   Programa para exibir a tabua de multiplicação de um número
'''

# Definição das variáveis
intMultiplicando = 1
intMultiplicador = 6

# Definição do laço de repetição
# Exibe a tabuada do 6 enquanto o multiplicando for menor ou igual a 10
while intMultiplicando <= 10:
   # Cálculo do produto
   intProduto = intMultiplicador * intMultiplicando
   # Exibição do resultado
   print(f'{intMultiplicador} x {intMultiplicando} = {intProduto}')
   # Incremento do multiplicando
   intMultiplicando += 1