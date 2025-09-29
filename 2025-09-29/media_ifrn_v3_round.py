'''
   Faça um programa para calcular média de uma disciplina no IFRN,
   sabendo que são duas notas e que o peso da primeira nota é 2
   e o peso da segunda nota é 3.
'''

# Informando as notas como números inteiros
intNota1 = int(input('Informe a nota da ETAPA 1:'))
intNota2 = int(input('Informe a nota da ETAPA 2:'))

# Calculando a média ponderada e arrendondando 
# para o inteiro mais próximo
intMedia = round( (intNota1*2 + intNota2*3) / 5)

# Mostrando as notas e a média
print(f'Nota da Etapa 1: {intNota1}')
print(f'Nota da Etapa 2: {intNota2}')
print(f'Média: {intMedia}')