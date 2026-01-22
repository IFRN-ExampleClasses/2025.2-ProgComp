import json

dictUFBR = {
    "AC": {"nome": "Acre", "capital": "Rio Branco", "região": "Norte"},
    "AL": {"nome": "Alagoas", "capital": "Maceió", "região": "Nordeste"},
    "AP": {"nome": "Amapá", "capital": "Macapá", "região": "Norte"},
    "AM": {"nome": "Amazonas", "capital": "Manaus", "região": "Norte"},
    "BA": {"nome": "Bahia", "capital": "Salvador", "região": "Nordeste"},
    "CE": {"nome": "Ceará", "capital": "Fortaleza", "região": "Nordeste"},
    "DF": {"nome": "Distrito Federal", "capital": "Brasília", "região": "Centro-Oeste"},
    "ES": {"nome": "Espírito Santo", "capital": "Vitória", "região": "Sudeste"},
    "GO": {"nome": "Goiás", "capital": "Goiânia", "região": "Centro-Oeste"},
    "MA": {"nome": "Maranhão", "capital": "São Luís", "região": "Nordeste"},
    "MT": {"nome": "Mato Grosso", "capital": "Cuiabá", "região": "Centro-Oeste"},
    "MS": {"nome": "Mato Grosso do Sul", "capital": "Campo Grande", "região": "Centro-Oeste"},
    "MG": {"nome": "Minas Gerais", "capital": "Belo Horizonte", "região": "Sudeste"},
    "PA": {"nome": "Pará", "capital": "Belém", "região": "Norte"},
    "PB": {"nome": "Paraíba", "capital": "João Pessoa", "região": "Nordeste"},
    "PR": {"nome": "Paraná", "capital": "Curitiba", "região": "Sul"},
    "PE": {"nome": "Pernambuco", "capital": "Recife", "região": "Nordeste"},
    "PI": {"nome": "Piauí", "capital": "Teresina", "região": "Nordeste"},
    "RJ": {"nome": "Rio de Janeiro", "capital": "Rio de Janeiro", "região": "Sudeste"},
    "RN": {"nome": "Rio Grande do Norte", "capital": "Natal", "região": "Nordeste"},
    "RS": {"nome": "Rio Grande do Sul", "capital": "Porto Alegre", "região": "Sul"},
    "RO": {"nome": "Rondônia", "capital": "Porto Velho", "região": "Norte"},
    "RR": {"nome": "Roraima", "capital": "Boa Vista", "região": "Norte"},
    "SC": {"nome": "Santa Catarina", "capital": "Florianópolis", "região": "Sul"},
    "SP": {"nome": "São Paulo", "capital": "São Paulo", "região": "Sudeste"},
    "SE": {"nome": "Sergipe", "capital": "Aracaju", "região": "Nordeste"},
    "TO": {"nome": "Tocantins", "capital": "Palmas", "região": "Norte"}
}

lstCenso2022 = [    ["AC",   830018], ["AL",  3127683], ["AP",   733508], 	
                    ["AM",  3941175], ["BA", 14136417], ["CE",  8791688], 	
                    ["DF",  2817068], ["ES",  3833486], ["GO",  7055228], 	
                    ["MA",  6775152], ["MT",  3658813], ["MS",  2756700],
                    ["MG", 20538718], ["PA",  8116132], ["PB",  3974495],  
                    ["PR", 11443208], ["PE",  9058155], ["PI",  3269200],
                    ["RJ", 16054524], ["RN",  3302406], ["RS", 10880506],
                    ["RO",  1581016], ["RR",   636303], ["SC",  7609601],
                    ["SP", 44420459], ["SE",  2209558], ["TO",  1511459]    ]

# dicionario[chave] = valor
# dicionario[UF]["população"] = valor

# Iterando o dicionário e atualizando com os dados da lista de censo
# Usando dois loops for
# Armazenando em variáveis para melhor entendimento
# chave = chave do dicionário (UF)
# valor = valor do dicionário (outro dicionário com nome, capital, região)
for chave, valor in dictUFBR.items():
   # Iterando a lista de censo
   for uf in lstCenso2022:
      # Verificando se a chave do dicionário é igual à UF da lista
      if chave == uf[0]:
         # Atualizando o dicionário com a população
         valor["população"] = uf[1]
         # Sai do loop interno
         break

# Convertendo o dicionário para JSON Nativo
dictUFBR = json.dumps(dictUFBR, ensure_ascii=False)

# Exibindo o dicionário atualizado
print(dictUFBR)

'''
    Usar a URL a seguir para visualizar os dados em formato JSON:

    https://jsonviewer.stack.hu/

    Copie e cole o conteúdo impresso no console na área esquerda do site.
    Clique em "Viewer" para visualizar os dados de forma estruturada.
'''