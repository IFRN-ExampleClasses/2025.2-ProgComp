'''
   Pesquise o que vem a ser List Comprehension em Python.

   Após a pesquisa, reescreva o código dos itens 1, e 7 utilizando List Comprehension.
'''
import random

intQtValores = 20

# ------------------------------------------------------------
# 1) Gerando a lista de valores únicos
lstValores = list()
i = 0
while i < intQtValores:
   intValor = random.randint(1, 100)
   if intValor not in lstValores:
      lstValores.append(intValor)
      i += 1 
print(f'Lista gerada.............: {lstValores}')

# ------------------------------------------------------------
# 2) Exibindo a soma dos valores na lista
intSoma = sum(lstValores)
print(f'Soma dos valores.........: {intSoma}')

# ------------------------------------------------------------
# 3) Exibindo a média dos valores na lista
fltMedia = intSoma / len(lstValores)
print(f'Média dos valores........: {fltMedia:.2f}')

# ------------------------------------------------------------
# 4) Exibindo o maior valor na lista
intMaior = max(lstValores)
print(f'Maior valor..............: {intMaior}')

# ------------------------------------------------------------
# 5) Exibindo o menor valor na lista
intMenor = min(lstValores)
print(f'Menor valor..............: {intMenor}')

# ------------------------------------------------------------
# 6) Exibindo a mediana dos valores na lista
lstOrdenada = sorted(lstValores)
print(f'Lista ordenada...........: {lstOrdenada}')

if len(lstOrdenada) % 2 == 1:
   fltMediana = lstOrdenada[len(lstOrdenada) // 2]
else:
   fltMediana = (lstOrdenada[len(lstOrdenada) // 2 - 1] + lstOrdenada[len(lstOrdenada) // 2]) / 2
print(f'Mediana dos valores......: {fltMediana}')

# ------------------------------------------------------------
# 7) Exibindo a variância dos valores na lista
fltVariancia = 0
for intValor in lstValores:
   fltVariancia += (intValor - fltMedia) ** 2
fltVariancia /= len(lstValores)
print(f'Variância dos valores....: {fltVariancia:.2f}')

# ------------------------------------------------------------
# 8) Exibindo o desvio padrão dos valores na lista
fltDesvioPadrao = fltVariancia ** 0.5
print(f'Desvio padrão dos valores: {fltDesvioPadrao:.2f}') 