'''
   Escreva um programa que construa uma lista de sub-listas de números inteiros.

   - O usuário deverá informar quantas sub-listas deseja gerar;
   - A primeira sub-lista será obrigatoriamente [1, 1];
   - Cada nova sub-lista deve começar e terminar com o número 1;
   - Os valores internos de cada sub-lista devem ser obtidos somando pares de números 
     vizinhos da sub-lista imediatamente anterior;
   - O processo deve continuar até que seja atingida a quantidade de sub-listas 
     definida pelo usuário;
   - Ao final, o programa deve imprimir todas as sub-listas geradas.

   Exemplo de saída para 5 sub-listas:

      [1, 1]
      [1, 2, 1]
      [1, 3, 3, 1]
      [1, 4, 6, 4, 1]
      [1, 5, 10, 10, 5, 1]
'''
import sys

try:
   intQuantidade = int(input('Quantas sub-listas deseja gerar? '))
except ValueError:
   sys.exit('Valor inválido. Informe um número inteiro.')
except Exception as e:
   sys.exit(f'Ocorreu um erro inesperado: {e}')
else:
   if intQuantidade <= 0:
      sys.exit('O número de sub-listas deve ser maior que zero.')

   lstListas   = [[1,1]]

   for i in range(1, intQuantidade):
      lstSubLista = [1]
      for j in range(len(lstListas[-1]) - 1):
         intSoma = lstListas[-1][j] + lstListas[-1][j + 1]
         lstSubLista.append(intSoma)
      lstSubLista.append(1)
      lstListas.append(lstSubLista)

   for subLista in lstListas:
      print(subLista)