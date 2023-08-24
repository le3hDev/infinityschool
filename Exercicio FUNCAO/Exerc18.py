"""
Faça uma função que recebe uma lista de números e retorna a soma dos números
negativos.
Exemplo de entrada: [-2, 3, -5, 7, -1]
Saída esperada: -8
"""

def soma_negativos(lista_numeros):
    soma = 0
    for numero in  lista_numeros:
        if numero< 0 :
            soma += numero
    return soma


numeros = [-2,  3, -5,  7, -1]
soma_negativos_resultantes = soma_negativos(numeros)
print (soma_negativos_resultantes)