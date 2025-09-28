

remetente = {

    "nome": "Fantasia",
    "rua": "Alfeneiros",
    "numero": 4,
    "bairro": "Little Whinging",
    "cidade": "Surrey",
    "estado": "PE",
    "cep":"53210091"
}

#print(remetente)

arquivo = open("clientes.txt", "r")
conteudo = arquivo.read()
arquivo.close()
#print(conteudo)

linhas = conteudo.split('\n')

#print("Conteúdo original:")
#print(conteudo)
#print("\nDepois do split:")
#print(linhas)

primeira_linha = linhas[0]
print("Linha original:", primeira_linha)

# Quebra pelos pontos-e-vírgulas
dados = primeira_linha.split('\;')  # Substitua ? pelo separador correto
print("Depois do split:", dados)