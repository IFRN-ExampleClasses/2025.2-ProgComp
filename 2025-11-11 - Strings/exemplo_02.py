'''
    Exemplo 02: Imprimindo um padrão de estrelas crescente e decrescente
'''

intQtEstrelas = 5

# Usando FOR
print('-'*80)
print('Usando FOR')
for i in range(1, intQtEstrelas+1):
    print('*'*i)

for i in range(intQtEstrelas-1, 0, -1):
    print('*'*i)


# Usando WHILE  
print('-'*80)
print('Usando WHILE')
i = 1 
while i <= intQtEstrelas:
    print('*'*i)
    i += 1

i = intQtEstrelas-1
while i > 0:
    print('*'*i)
    i -= 1