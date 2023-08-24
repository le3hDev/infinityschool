"""
Escreva uma função que recebe uma lista de números e retorna a quantidade de
números positivos.
Exemplo de entrada: [-2, 3, -5, 7, -1]
Saída esperada: 2
"""
def contar_positivos(lista_numeros):
    quantidade = 0
    for numero in lista_numeros:
        if numero > 0:
            quantidade += 1

    return quantidade


numeros = [-2, 3, -5, 7, -1]
quantidade_positivos = contar_positivos(numeros)
print(quantidade_positivos)