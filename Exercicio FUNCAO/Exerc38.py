"""
Crie uma função que recebe uma lista de palavras e retorna a quantidade de palavras
que contêm a letra "a".
Exemplo de entrada: ["casa", "carro", "python", "programação"]
Saída esperada: 3
"""

def contar_palavras_com_a(lista_palavras):
    quantidade = 0
    for palavra in lista_palavras:
        if "a" in palavra or "A" in palavra:
            quantidade += 1
    return quantidade

palavras = ["casa", "carro", "python", "programação"]
quantidade_palavras_com_a = contar_palavras_com_a(palavras)
print(quantidade_palavras_com_a)