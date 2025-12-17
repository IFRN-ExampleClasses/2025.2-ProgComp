'''
   Fazer um programa que leia o arquivo valores_1.txt, que contém números 
   inteiros, um por linha, gere uma lista contendo os números lidos e em seguida
   calcule a soma desses números. O programa deve exibir o resultado na tela.
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

   # Imprimindo o conteúdo lido na tela
   print(lstNumeros)

