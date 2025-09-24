ano_atual      = 2025
ano_nascimento = int(input('Em que ano você nasceu? '))

idade          = ano_atual - ano_nascimento

# Você tem 51 anos.
print('Você tem', idade, 'anos.')

print('Você tem ' + str(idade) + ' anos.')

print(f'Você tem {idade} anos.')

# Você nasceu em 1974 e tem 51 anos.
print('Você nasceu em', ano_nascimento, 'e tem', idade, 'anos.')

print('Você nasceu em ' + str(ano_nascimento) + ' e tem ' + str(idade) + ' anos.')

print(f'Você nasceu em {ano_nascimento} e tem {idade} anos.')