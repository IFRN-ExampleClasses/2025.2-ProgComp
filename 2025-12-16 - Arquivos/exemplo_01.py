'''
   Fazer um programa que leia o arquivo valores_1.txt, que contém números 
   inteiros, um por linha, gere uma lista contendo os números lidos.
   
   Após a leitura, calcule:

   a) A soma dos números;
   b) A média dos números;
   c) Quantos números são maiores que média;
   d) Quantos números são menores que média;
   e) A mediana dos números;
   f) A variância dos números;
   g) O desvio padrão dos números.

   Escreva os resultados em um arquivo chamado resultados.txt.
'''
# Importando o módulo os para manipulação de caminhos de arquivos
import os, sys

# Obtendo o diretório do arquivo atual
strDiretorio = os.path.dirname(__file__)

# Definindo o nome do arquivo a ser lido
strNomeArquivo = 'valores_1.txt'

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
         continue
      except Exception as e:
         # Tratando outros erros genéricos
         print(f'ERRO: {e} ao processar o valor "{strLinha}" ignorado!')
         continue
      
      # Adicionando o valor lido convertido em inteiro à lista
      lstNumeros.append(intValor)

   # Fechando o arquivo após a leitura
   arqLeitura.close()
