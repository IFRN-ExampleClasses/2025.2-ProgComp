'''
   Faça um programa que solicite ao usuário um número inteiro e 
   informe em quantas interções ele converge para a constante de 
   Kaprekar (6174). Lembre-se que o número deve ter 4 dígitos 
   distintos. Caso o número não atenda a essa condição, informe
   que ele é inválido.

   O que é a constante de Kaprekar?
   A constante de Kaprekar é o número 6174, que é alcançado através
   de um processo repetitivo de manipulação de números de 4 dígitos.

   Como funciona o processo de Kaprekar:
   1. Pegue qualquer número de 4 dígitos com pelo menos dois dígitos diferentes.
   2. Ordene os dígitos em ordem crescente e decrescente para formar dois números diferentes.
   3. Subtraia o menor número do maior número.
   4. Repita o processo com o resultado até chegar a 6174.

   Exemplo:
   - Comece com o número 3524.
   - Ordene os dígitos: 5432 (decrescente) e 2345 (crescente).
     1ª iteração: 5432 - 2345 = 3087
   - Repita o processo:
     2ª iteração: 8730 - 0378 = 8352
     3ª iteração: 8532 - 2358 = 6174
'''