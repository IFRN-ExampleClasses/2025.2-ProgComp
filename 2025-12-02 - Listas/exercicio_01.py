'''
   Escreva um programa que construa uma lista de sub-listas de números inteiros.

   - O usuário deverá informar quantas sub-listas deseja gerar;
   - A primeira sub-lista deve ser [1, 1];
   - Cada nova sub-lista deve ser formada acrescentando ao final da lista anterior 
     a soma dos dois últimos números já existentes;
   - O processo deve continuar até que seja atingida a quantidade de sub-listas 
     definida pelo usuário.
   - Ao final, o programa deve imprimir todas as sub-listas geradas.

   Exemplo de saída para 5 sub-listas:

      [1, 1]
      [1, 1, 2]
      [1, 1, 2, 3]
      [1, 1, 2, 3, 5]
      [1, 1, 2, 3, 5, 8]
'''
import sys

try:
   intQuantidade = int(input('Quantas sub-listas deseja gerar? '))
except ValueError:
   sys.exit('Valor inválido. Por favor, insira um número inteiro.')
except Exception as e:    
   sys.exit(f'Ocorreu um erro inesperado: {e}')
else:
   if intQuantidade <= 0:
      sys.exit('Por favor, insira um número inteiro positivo.')

   lstLista = [ [1,1] ]

   for _ in range(intQuantidade):
      lstLista.append( lstLista[-1] + [ lstLista[-1][-1] + lstLista[-1][-2] ] )
   
   for lstSubLista in lstLista:
      print(lstSubLista)