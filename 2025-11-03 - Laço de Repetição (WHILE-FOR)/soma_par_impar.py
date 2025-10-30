'''
   Reescreva o programa a seguir usando o laço FOR.
'''

# Inicialização das variáveis
intSomaPares   = 0
intSomaImpares = 0
intContador    = 1

# Laço de repetição para contar de 1 a 100
while intContador <= 100:
   # Verifica se o número é par ou ímpar e acumula a soma
   if intContador % 2 == 0:
      intSomaPares += intContador
   else:
      intSomaImpares += intContador

   # Incrementa o contador
   intContador += 1

# Exibição dos resultados
print(f'Soma dos números pares....: {intSomaPares}')
print(f'Soma dos números ímpares .: {intSomaImpares}')