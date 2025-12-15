'''
   Fazer um programa que leia o conteúdo do arquivo resumo_lotr.txt e imprima na tela.
'''
# Importando o módulo os para manipulação de caminhos de arquivos
import os, sys

# Obtendo o diretório do arquivo atual
strDiretorio = os.path.dirname(__file__)

# Definindo o nome do arquivo a ser lido
strNomeArquivo = 'resumo_lotr.txt'

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
   # Lendo o conteúdo do arquivo
   strConteudo = arqLeitura.read()

   # Fechando o arquivo após a leitura
   arqLeitura.close()
   
   # Imprimindo o conteúdo lido na tela
   print(strConteudo)

