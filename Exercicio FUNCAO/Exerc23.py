"""
Crie uma função que recebe uma lista de números e retorna uma nova lista com os
números em ordem decrescente.
Exemplo de entrada: [3, 1, 4, 2]
Saída esperada: [4, 3, 2, 1]
"""
def ordenar_decrescente(lista_numeros):
    for i in range(len(lista_numeros)):
        for j in range(0, len(lista_numeros) - i - 1):
            if lista_numeros[j] < lista_numeros[j + 1]:
                lista_numeros[j], lista_numeros[j + 1] = lista_numeros[j + 1], lista_numeros[j]
    return lista_numeros

numeros = [3, 1, 4, 2]
numeros_ordenados = ordenar_decrescente(numeros)
print(numeros_ordenados) 