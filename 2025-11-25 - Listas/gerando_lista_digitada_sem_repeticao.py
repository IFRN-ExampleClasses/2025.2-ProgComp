# Declara uma lista vazia para armazenar os valores digitados pelo usuário
lstValores = list()

# Inicializa a variável de controle (-1 para entrar no loop)
intValor = -1

# Loop para solicitar números inteiros ao usuário até que ele digite 0
while intValor != 0:
   try:
      intValor = int(input('Informe um número inteiro (0 para sair): '))
   except ValueError:
      print('ERRO: Valor inválido. Por favor, informe um número inteiro...\n')
   except Exception as e:
      print(f'ERRO: Ocorreu um erro inesperado: {e}\n')
   else:
      if intValor == 0:
         print('Foi informado o valor 0. Encerrando o programa...\n')
      elif intValor > 0:
         # Adiciona o valor na lista apenas se não estiver presente
         if intValor not in lstValores:
            print(f'O número {intValor} é positivo e não está na lista... Será adicionado na lista.\n')
            lstValores.append(intValor)
         else:
            print(f'O número {intValor} já está na lista. Não será adicionado novamente.\n')
      else:
         print(f'O número {intValor} é negativo... Não será adicionado na lista.\n')

# Exibe a lista de valores informados pelo usuário
print('Lista de valores informados:')
print(lstValores)

# Exibir a soma dos valores na lista

# Exibir a média dos valores na lista

# Exibir o maior valor na lista e sua posição

# Exibir o menor valor na lista e sua posição

