'''
    Exemplo 01: Imprimindo um padrão de estrelas crescente
'''

intQtEstrelas = 5

# Usando FOR
print('-'*80)
print('Usando FOR')
for i in range(1, intQtEstrelas+1):
    print('*'*(i))


# Usando WHILE
print('-'*80)
print('Usando WHILE')
i = 1 
while i <= intQtEstrelas:
    print('*'*i)
    i += 1