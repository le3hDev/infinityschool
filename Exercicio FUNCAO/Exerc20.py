"""
Crie uma função que recebe uma lista de palavras e retorna a quantidade de palavras
que começam com a letra "a".
Exemplo de entrada: ["amor", "casa", "arroz", "banana"]
Saída esperada: 2
"""
def contar_palavras_comecando_com_a(lista_palavras):
    quantidade = 0
    for palavra in lista_palavras:
        if len(palavra) > 0 and (palavra[0] == "a" or palavra[0] == "A"):
            quantidade += 1
    return quantidade

palavras = ["amor", "casa", "arroz", "banana"]
quantidade_palavras_a = contar_palavras_comecando_com_a(palavras)
print(quantidade_palavras_a)  