"""
Escreva uma função que recebe uma lista de números e retorna a soma dos números
pares e a soma dos números ímpares separadamente.
Exemplo de entrada: [1, 2, 3, 4, 5, 6]
Saída esperada: Soma dos pares: 12, Soma dos ímpares: 9
"""
def somar_pares_impares(lista_numeros):
    soma_pares = 0
    soma_impares = 0
    
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma_pares += numero
        else:
            soma_impares += numero
    
    return soma_pares, soma_impares

numeros = [1, 2, 3, 4, 5, 6]
soma_pares, soma_impares = somar_pares_impares(numeros)
print("Soma dos pares:", soma_pares)
print("Soma dos ímpares:", soma_impares)
