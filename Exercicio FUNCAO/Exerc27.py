"""
Faça uma função que recebe uma lista de números e retorna a soma dos números
positivos e a soma dos números negativos separadamente.
Exemplo de entrada: [1, -2, 3, -4, 5]
Saída esperada: Soma dos positivos: 9, Soma dos negativos: -6
"""
def somar_positivos_negativos(lista_numeros):
    soma_positivos = 0
    soma_negativos = 0
    
    for numero in lista_numeros:
        if numero > 0:
            soma_positivos += numero
        elif numero < 0:
            soma_negativos += numero
    
    return soma_positivos, soma_negativos

numeros = [1, -2, 3, -4, 5]
soma_positivos, soma_negativos = somar_positivos_negativos(numeros)
print("Soma dos positivos:", soma_positivos)
print("Soma dos negativos:", soma_negativos)
