'''
   Fazer um programa que leia o arquivo valores_1.txt, que contém números 
   inteiros, um por linha, gere uma lista contendo os números lidos.
   
   Após a leitura, calcule:

   a) A soma dos números;
   b) A média dos números;
   c) Quantos números são maiores ou iguais a média;
   d) Quantos números são menores que média;
   e) A mediana dos números;
   f) A variância dos números;
   g) O desvio padrão dos números.

   Escreva os resultados em um arquivo chamado resultados.txt.
'''
# Importando o módulo os para manipulação de caminhos de arquivos
import os, sys, statistics

# Obtendo o diretório do arquivo atual
strDiretorio = os.path.dirname(__file__)

# Definindo o nome do arquivo a ser lido
strNomeArquivo = 'valores_2.txt'

try:
   # Tentando abrir o arquivo no modo de leitura
   arqLeitura = open(f'{strDiretorio}/{strNomeArquivo}', 'r', encoding='utf-8')
except FileNotFoundError:
   # Tratando o erro caso o arquivo não seja encontrado
   sys.exit(f'ERRO: Arquivo "{strNomeArquivo}" não encontrado!')
except Exception as e:
   # Tratando outros erros genéricos
   sys.exit(f'ERRO: {e}')
else:
   # Criando uma lista que irá guardar os números
   lstNumeros = list()

   # Lendo o conteúdo do arquivo
   intErros = 0
   while True:
      # Lendo uma linha do arquivo e removendo caracteres 
      # de espaço em branco e caractere de nova linha (\n)
      strLinha = arqLeitura.readline().strip()

      # Verificando se chegou ao final do arquivo
      if not strLinha: break

      # Convertendo a linha lida para inteiro
      try:
         intValor = int(strLinha)
      except ValueError:
         # Tratando o erro caso a conversão falhe
         print(f'ERRO: Valor inválido "{strLinha}" ignorado!')
         intErros += 1
         continue
      except Exception as e:
         # Tratando outros erros genéricos
         print(f'ERRO: {e} ao processar o valor "{strLinha}" ignorado!')
         intErros += 1
         continue
      
      # Adicionando o valor lido convertido em inteiro à lista
      lstNumeros.append(intValor)

   # Fechando o arquivo após a leitura
   arqLeitura.close()

   # a) Calculando a soma dos números
   intSoma         = sum(lstNumeros)

   # b) Calculando a média dos números 
   fltMedia        = intSoma / len(lstNumeros)   

   # c) Contando quantos números são maiores ou iguais a média
   # Resolver em uma linha de código
   
   # d) Contando quantos números são menores que a média
   # Resolver em uma linha de código

   # e) Calculando a mediana dos números
   fltMediana      = statistics.median(lstNumeros)

   # f) Calculando a variância dos números
   fltVariancia    = statistics.variance(lstNumeros)

   # g) Calculando o desvio padrão dos números
   fltDesvioPadrao = statistics.stdev(lstNumeros)

   # Definindo o nome do arquivo de resultados
   strNomeArquivoResultados = ''

   # Abrindo o arquivo de resultados no modo de escrita
   try:
      arqResultados = open(f'{strDiretorio}/resultados.txt', 'w', encoding='utf-8')
   except Exception as e:
      sys.exit(f'ERRO: {e}')      
   else:
      arqResultados.write(f'Soma............: {intSoma}\n')
      arqResultados.write(f'Média...........: {fltMedia}\n')
      arqResultados.write(f'Mediana.........: {fltMediana}\n')
      arqResultados.write(f'Variância.......: {fltVariancia}\n')
      arqResultados.write(f'Desvio Padrão...: {fltDesvioPadrao}\n')
      arqResultados.write(f'Linhas Ignoradas: {intErros}\n')

      # Fechando o arquivo de resultados após a escrita
      arqResultados.close()