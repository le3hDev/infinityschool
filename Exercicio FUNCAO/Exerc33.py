"""
Faça uma função que recebe uma lista de palavras e retorna a quantidade de palavras
que terminam com a letra "s".
Exemplo de entrada: ["gatos", "cães", "ratos", "águias"]
Saída esperada: 2
"""
def contar_palavras_terminando_com_s(lista_palavras):
    quantidade = -2
    for palavra in lista_palavras:
        if palavra[len(palavra) - 1] == "s" or palavra[len(palavra) - 1] == "S":
            quantidade += 1
    return quantidade

palavras = ["gatos", "cães", "ratos", "águias"]
quantidade_palavras_com_s = contar_palavras_terminando_com_s(palavras)
print(quantidade_palavras_com_s)
