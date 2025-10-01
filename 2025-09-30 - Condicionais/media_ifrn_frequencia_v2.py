'''
   Faça um programa para calcular média e a frequência de uma disciplina 
   no IFRN.

   Sabe-se que são duas notas e que o peso da primeira nota é 2
   e o peso da segunda nota é 3. 

   Sabe-se também que para se calcular a frequência, deve-se informar a carga 
   horária da disciplina (em horas/aula) e a quantidade de faltas do aluno.

   - Teste 1: Nota1 = 50 e Nota2 = 65
   - Teste 2: Nota1 = 73 e Nota2 = 19
   - Teste 3: Nota1 = 72 e Nota2 = 29
   - Teste 4: Nota1 = 10 e Nota2 = 21
'''
import sys

# Informando a nota 1 como número inteiro
intNota1 = int(input('Informe a nota da ETAPA 1: '))

# Saindo do programa se a nota 1 for inválida
if not (intNota1>=0 and intNota1<=100):
   sys.exit('Nota 1 inválida! Deve ser entre 0 e 100.')

# Informando a nota 2 como número inteiro
intNota2 = int(input('Informe a nota da ETAPA 2: '))

# Saindo do programa se a nota 2 for inválida
if not (intNota2>=0 and intNota2<=100):
   sys.exit('Nota 2 inválida! Deve ser entre 0 e 100.')

# Informando a carga horária da disciplina (horas/aula)
intCargaHoraria = int(input('Informe a Carga Horária da Disciplina (h/a): '))

#TODO: Validar se a carga horária é maior que zero e menor ou igual a 360

# Informando a quantidade de faltas do aluno
intFaltas = int(input('Informe a quantidade de faltas do aluno: '))

# TODO: Validar se a quantidade de faltas é maior ou igual a zero
# e menor ou igual a carga horária

# Calculando a média ponderada e arredondando 
# para o inteiro mais próximo
intMedia = round( (intNota1*2 + intNota2*3) / 5)

# Calculando a frequência do aluno
fltFrequencia = round( (1 - (intFaltas / intCargaHoraria)) * 100, 1)

# Mostrando as notas e a média
print(f'Nota da Etapa 1: {intNota1}')
print(f'Nota da Etapa 2: {intNota2}')
print(f'Média..........: {intMedia}')

# Mostrar a Frequência
print(f'Total de Aulas.: {intCargaHoraria}')
print(f'Total de Faltas: {intFaltas}')
print(f'Frequência.....: {fltFrequencia}%')

# Mostrando se o aluno está APROVADO, PROVA FINAL ou REPROVADO
# TODO: implementar a lógica para mostrar se o aluno foi 
# reprovado por nota, por frequência ou por ambos
if (intMedia >= 60) and (fltFrequencia>=75):
   print('APROVADO')
elif (intMedia >= 20) and (fltFrequencia>=75):
   print('PROVA FINAL')
else:
   print('REPROVADO')