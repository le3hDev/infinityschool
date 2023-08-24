"""
Crie uma função que recebe uma lista de strings e retorna a quantidade de palavras que
têm um número ímpar de letras.
Exemplo de entrada: ["python", "programação", "é", "divertida"]
Saída esperada: 3
"""
def contar_palavras_com_numero_impar_de_letras(lista_palavras):
    quantidade = 0
    for palavra in lista_palavras:
        if len(palavra) % 2 != 0:
            quantidade += 1
    return quantidade

palavras = ["python", "programação", "é", "divertida"]
quantidade_palavras_impar_de_letras = contar_palavras_com_numero_impar_de_letras(palavras)
print(quantidade_palavras_impar_de_letras)