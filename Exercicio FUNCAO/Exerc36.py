"""
Faça uma função que recebe uma lista de números e retorna a quantidade de números
negativos.
Exemplo de entrada: [-2, 3, -5, 7, -1]
Saída esperada: 3
"""
def contar_numeros_negativos(lista_numeros):
    quantidade = 0
    for numero in lista_numeros:
        if numero < 0:
            quantidade += 1
    return quantidade

numeros = [-2, 3, -5, 7, -1]
quantidade_numeros_negativos = contar_numeros_negativos(numeros)
print(quantidade_numeros_negativos)  
