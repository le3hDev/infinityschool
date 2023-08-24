"""
Escreva uma função que recebe uma lista de palavras e retorna quantas delas têm mais
de 5 caracteres.
Exemplo de entrada: ["python", "programação", "é", "divertida"]
Saída esperada: 2
"""
def palavras_longas(lista_palavras):
    contador = 0
    for palavra in lista_palavras:
        if len(palavra) > 6:
            contador += 1
    return contador

entrada = ["python", "programação", "é", "divertida"]
saida = palavras_longas(entrada)
print(saida)        