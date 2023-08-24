"""
Escreva uma função que recebe uma lista de números e retorna a soma dos números
positivos multiplicada pela soma dos números negativos.
Exemplo de entrada: [1, -2, 3, -4, 5]
Saída esperada: -12
"""
def calcular_soma_positivos_mult_soma_negativos(lista_numeros):
    soma_positivos = 0
    soma_negativos = 0
    
    for numero in lista_numeros:
        if numero > 0:
            soma_positivos += numero
        elif numero < 0:
            soma_negativos += numero
    
    return soma_positivos * soma_negativos

numeros = [1, -2, 3, -4, 5]
resultado_final = calcular_soma_positivos_mult_soma_negativos(numeros)
print(resultado_final)  # Deverá imprimir -12
