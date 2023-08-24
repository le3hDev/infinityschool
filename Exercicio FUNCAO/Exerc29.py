""""
Crie uma função que recebe uma lista de números e retorna o produto de todos os
elementos.
Exemplo de entrada: [2, 3, 4]
Saída esperada: 24
"""
def calcular_produto(lista_numeros):
    produto = 1
    for numero in lista_numeros:
        produto *= numero
    return produto

numeros = [2, 3, 4]
produto_resultante = calcular_produto(numeros)
print(produto_resultante)  