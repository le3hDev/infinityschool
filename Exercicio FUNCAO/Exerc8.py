"""
Crie uma função que recebe uma lista de números e retorna uma nova lista com apenas
os números pares.
Exemplo de entrada: [1, 2, 3, 4, 5, 6]
Saída esperada: [2, 4, 6]
"""
def numeros_pares(lista_numeros):
    return [numero for numero in lista_numeros if numero % 2 == 0]


entrada = [1, 2, 3, 4, 5, 6]
saida = numeros_pares(entrada)
print(saida)
