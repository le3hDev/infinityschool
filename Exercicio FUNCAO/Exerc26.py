"""
Crie uma função que recebe uma lista de palavras e retorna a quantidade de palavras
que têm um número par de letras.
Exemplo de entrada: ["casa", "carro", "python", "programação"]
Saída esperada: 2
"""
def contar_palavras_com_numero_par_de_letras(lista_palavras):
    quantidade = 0
    for palavra in lista_palavras:
        if len(palavra) % 2 == 0:
            quantidade += 1
    return quantidade

palavras = ["casa", "carro", "python", "programação"]
quantidade_palavras_par_de_letras = contar_palavras_com_numero_par_de_letras(palavras)
print(quantidade_palavras_par_de_letras)  