'''
   Reescreva o código do exercício anterior, mas desta vez utilizando listas
   compostas (listas dentro de listas) para armazenar as informações dos alunos.
'''
lstAlunos = list()

intAlunos = 1
while intAlunos <= 5:
   strNome  = input(f'\nDigite o nome do {intAlunos}º aluno: ')
   try:
      intNota1 = int(input(f'Digite a nota da Etapa 1: '))
      intNota2 = int(input(f'Digite a nota da Etapa 2: '))
   except ValueError:
      print('ERRO: Digite um valor inteiro para a nota.')
      continue
   else:
      if (intNota1 < 0 or intNota1 > 100):
         print('ERRO: A nota da Etapa 1 deve estar entre 0 e 100.')
         continue

      if (intNota2 < 0 or intNota2 > 100):
         print('ERRO: A nota da Etapa 2 deve estar entre 0 e 100.')
         continue
   
      intMedia = round(((intNota1 * 2) + (intNota2 * 3)) / 5)
      lstAlunos.append([strNome, intNota1, intNota2, intMedia])

      intAlunos += 1

lstAlunos.sort()

print(f'{"Nome do Aluno":<30} {"Etapa 1":>8} {"Etapa 2":>8} {"Média":>8}')
print('-' * 60)
for alunos in lstAlunos:
   print(f'{alunos[0]:<30} {alunos[1]:>8} {alunos[2]:>8} {alunos[3]:>8}')
print('-' * 60)
