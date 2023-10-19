lista = [ [1122,"Ana Rocha", "1111-1111", "F", "Eng. de Software" ],
            [3344,"Bruna Lima", "2222-2222", "F", "Eng. Mecatrônica"] ]

dicionario = { 1122: ["Ana Rocha", "1111-1111", "F", "Eng. de Software"],
                3344: ["Bruna Lima", "2222-2222", "F", "Eng. Mecatrônica"]}
print(dicionario.get(1122))
if 1314 in dicionario:
    print("Chave existe")
else:
    print("Chave NAO existe")
print(dicionario.get(1314))
#print(dicionario[1314])
dicionario.update({1314:["Leila Campos", "6666-6666", "F", "Eng. Elétrica"]})
print(dicionario.get(1314))
print(len(dicionario))
if 1314 in dicionario:
    print("Chave existe")
else:
    print("Chave NAO existe")