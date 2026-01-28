'''
   Abrindo o arquivo times_brasileirao.json em modo de leitura

   e imprimindo seu conteúdo na tela.
'''
import sys, os, json

strDiretorio = os.path.dirname(__file__)
strArquivo   = 'times_brasileirao.json'

try:
   arqLeitura = open(f'{strDiretorio}/{strArquivo}', 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit(f'Arquivo {strArquivo} não encontrado para leitura.')
except Exception as e:
   sys.exit(f'Erro ao abrir o arquivo {strArquivo} para leitura: {e}')
else:
   dictDados = json.dumps(json.load(arqLeitura), ensure_ascii=False)
   arqLeitura.close()
   
   print(dictDados)
 
   '''
      Filtrar as estatisticas dos times para o ano informado
   '''
   intAno = 2025   

   # 1. Percorrer os dados e apagar os anos diferentes do informado

   # 2. Criar um novo dicionário para armazenar apenas os dados do ano informado
   #    de cada time
   
   # 3. Filtrar os dados para manter apenas os dicionários do ano informado
   #    de cada time
