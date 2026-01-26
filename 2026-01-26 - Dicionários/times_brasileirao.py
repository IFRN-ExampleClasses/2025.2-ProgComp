'''
   Ler o arquivo Brasileirao_Serie_A.csv e gerar um 
   dicionário com os nomes dos times como chaves e um dicionário
   como valor contendo 'Ano', 'Vitórias', 'Empates', 'Derrotas', 
   'Gols Pró', 'Gols Contra', 'Cartões Amarelos' e 'Cartões Vermelhos'.
'''
import os, sys, json

strDiretorio   = os.path.dirname(__file__)
strNomeArquivo = f'{strDiretorio}/Brasileirao_Serie_A.csv'

intAno = 2025

try:
   arqEntrada = open(strNomeArquivo, 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('Erro: O arquivo não foi encontrado.')
except Exception as e:
   sys.exit(f'Erro ao abrir o arquivo: {e}')
else:
   # Ler a primeira linha para obter as chaves do dicionário interno
   lstChaves = arqEntrada.readline().strip().split(';')
   
   # Remover a chave 'Time' que não será usada no dicionário interno
   lstChaves.pop(0)

   # Inicializar o dicionário principal
   dictTimes= dict()

   while True:
      # Lendo os dados de cada time
      strLinha = arqEntrada.readline().strip()
      
      # Verificar se chegou ao final do arquivo
      if not strLinha: break

      # Dividir a linha em uma lista de dados
      lstDados = strLinha.split(';')
      
      # Chave de dictClassificacao -> Nome do time
      strTime = lstDados[0]
      
      # Eliminar o nome do time da lista de dados
      lstDados.pop(0)

      # Criar o dicionário de cada time associando chaves e valores
      dictInfoTime = dict(zip(lstChaves, lstDados))

      # Adicionar o dicionário do time ao dicionário principal
      dictTimes[strTime] = dictInfoTime

   # Fechar o arquivo após a leitura
   arqEntrada.close()

   # Exibir o dicionário resultante
   print(dictTimes)

   print(len(dictTimes), 'times no dicionário.')