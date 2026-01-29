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
   dictDados = json.load(arqLeitura)
   arqLeitura.close()
   
   '''
      Filtrar as estatisticas dos times para o ano informado
   '''
   intAno = 2025   

   # 1. Percorrer os dados e criar um novo dicionário para armazenar 
   # apenas os dados do ano informado de cada time
   dictDadosAno = dict()
   for strTime, lstEstatisticas in dictDados.items():
      for dictEstatisticas in lstEstatisticas:
         if dictEstatisticas['Ano'] == intAno:
            dictDadosAno[strTime] = dictEstatisticas
            break
   
   # 2. Ordenar o novo dicionário pela pontuação do time
   dictClassificacao = dict(sorted(dictDadosAno.items(), 
                              key=lambda item: (item[1]['Pontuacao'], item[1]['Gols_Pro']),
                              reverse=True))

   # 3. Gravar o novo dicionário em um novo arquivo JSON
   arqEscrita = open(f'{strDiretorio}/times_brasileirao_{intAno}.json', 'w', encoding='utf-8')
   json.dump(dictClassificacao, arqEscrita, ensure_ascii=False, indent=4)
   arqEscrita.close()
