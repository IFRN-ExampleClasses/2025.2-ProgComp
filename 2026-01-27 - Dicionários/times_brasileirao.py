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
      dictInfoAno = dict(zip(lstChaves, lstDados))

   # ------------------------------------------------------------
   # Aula dia 27/01/2026 - Início da modificação

      # Convertendo os valores numéricos de string para inteiro
      for strChave in dictInfoAno.keys():
         if dictInfoAno[strChave].isdigit():
            dictInfoAno[strChave] = int(dictInfoAno[strChave])

      # Adicionar a pontuação do ano atual nos dicionários
      # A pontuação é calculada como: Vitórias * 3 + Empates
      dictInfoAno['Pontuacao'] = dictInfoAno['Vitorias'] * 3 + dictInfoAno['Empates']

      # Adicionar o saldo de gols nos dicionários
      dictInfoAno['SaldoGols'] = dictInfoAno['Gols_Pro'] - dictInfoAno['Gols_Contra']
 
      # Verifica se o time já consta nas chaves do dicionário
      if not strTime in dictTimes.keys():
         # Se não existe, cria uma nova lista contendo o dicionário
         dictTimes[strTime] = [dictInfoAno]
      else:
         # Se já existe, recupera a lista e adiciona o novo ano
         dictTimes[strTime].append(dictInfoAno)

   # Aula dia 27/01/2026 - Fim da modificação
   # ------------------------------------------------------------

   # Fechar o arquivo após a leitura
   arqEntrada.close()

   # Convertendo o dicionário (aspas simples) para JSON Nativo (aspas duplas)
   # ensure_ascii=False permite que os acentos sejam exibidos corretamente
   dictTimes = json.dumps(dictTimes, ensure_ascii=False, indent=4)

   # Salvar o dicionário em um arquivo JSON
   strNomeArquivoSaida = f'{strDiretorio}/times_brasileirao.json'
   try:
      arqSaida = open(strNomeArquivoSaida, 'w', encoding='utf-8')
   except Exception as e:
      sys.exit(f'Erro ao salvar o arquivo JSON: {e}')
   else:
      arqSaida.write(dictTimes)
      arqSaida.close()