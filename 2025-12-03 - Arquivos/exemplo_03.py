# Gerando uma lista com os valores de 1 a 20 e seus respectivos fatoriais
lstValores = list()

for i in range(1, 21):
   x = 1
   for j in range(1, i+1):
      x *= j
   lstValores.append([i, x])

# Escrevendo os valores em um arquivo texto
arqSaida = open('fatoriais.csv', 'a')
for lista in lstValores:
   arqSaida.write(f'{lista[0]};{lista[1]}\n')
arqSaida.close()