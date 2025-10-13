'''
   Faça um programa que solicite ao usuário um número de até 4 dígitos 
   inteiro positivo e exiba a soma dos seus algarismos.

   Exemplo: 2456 = 17 (2 + 4 + 5 + 6)

   DICA: Vocês irão usar o operador de divisão inteira (//) e o operador 
   de resto de divisão inteiro (%)
'''
import sys

num = int(input('Digite um número inteiro positivo de até 4 dígitos: '))

if num < 0 or num > 9999:
   sys.exit('Número inválido. Por favor, digite um número entre 0 e 9999.')  

intMilhar = num // 1000
restoMilhar = num % 1000

intCentena = restoMilhar // 100
restoCentena = restoMilhar % 100

intDezena = restoCentena // 10
intUnidade = restoCentena % 10

soma = intMilhar + intCentena + intDezena + intUnidade