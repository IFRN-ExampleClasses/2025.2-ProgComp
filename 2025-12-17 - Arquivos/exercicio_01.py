'''
   Fazer um programa que leia o arquivo capitais_brasil.csv e
   preencha uma lista com sublistas contendo o nome da capital, 
   a sigla do seu estado, a sigla da sua região e a sua população.

   Após gerar a lista, gere uma lista contendo a sigla da região
   e o total da população das capitais daquela região.

   Em seguida salve o resultado em um arquivo chamado populacao_regioes.csv,
   no mesmo diretório onde se encontra o programa, no seguinte formato 
   (os valores abaixo são apenas ilustrativos):

   Região;População
   N;123456
   NE;234567
   CO;345678
   S;456789
   SE;567890
   
   Não use bibliotecas para manipulação de arquivos CSV.
'''
import os, sys

# Definindo os nomes dos arquivos
strArquivoEntrada = 'capitais_brasil.csv'
strArquivoSaida   = 'populacao_regioes.csv'

# Obtendo o diretório atual (opcional)
strDirAtual = os.path.dirname(__file__)

# Lista principal para armazenar as sublistas (Capital, UF, Regiao, Populacao)
lstCapitais = list()

try:
   # Abre o arquivo de entrada manualmente
   arqEntrada = open(f'{strDirAtual}/{strArquivoEntrada}', 'r', encoding='utf-8')
except FileNotFoundError as erroArquivo:
   sys.exit(f'ERRO: Arquivo "{strArquivoEntrada}" nao encontrado...')
except Exception as erroGeral:
   sys.exit(f'ERRO: {erroGeral}...')
else:
   # Iniciando a leitura do arquivo
   while True:
      # Lendo uma linha do arquivo
      strLinha = arqEntrada.readline().strip()
   
      # Verificando se chegou ao final do arquivo
      if not strLinha: break

      # Divide a linha pelo separador
      lstPartesLinha = strLinha.split(';')

      # Adicionando a sublista na lista principal
      lstCapitais.append(lstPartesLinha)
   
   # Fechando o arquivo de entrada
   arqEntrada.close()
 
   # Montando uma lista com as siglas das regiões. O índice 2 é a sigla da região
   lstRegioes = list()
   for lstCapital in lstCapitais: 
      if lstCapital[2] not in lstRegioes:
         lstRegioes.append(lstCapital[2])

   # Calculando a população total por região utilizando lista de regiões
   # e filter() na lista de capitais
   lstPopulacaoRegioes = list()
   for strRegiao in lstRegioes:
      # Filtrando as capitais da região atual
      lstCapitaisRegiao = list(filter(lambda x: x[2] == strRegiao, lstCapitais))
      
      # Somando a população das capitais da região atual
      intPopulacaoTotal = sum(int(lstCapital[3]) for lstCapital in lstCapitaisRegiao)
      
      # Adicionando o resultado na lista de populações por região
      lstPopulacaoRegioes.append([strRegiao, intPopulacaoTotal])
   
   print('População por Região:')
   for lstRegiao in lstPopulacaoRegioes:
      print(f'Região: {lstRegiao[0]} - População: {lstRegiao[1]}')