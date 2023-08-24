"""
Escreva uma função que recebe uma lista de números e retorna a soma dos dígitos de
cada número.
Exemplo de entrada: [10, 22, 345, 9]
Saída esperada: [1, 4, 12, 9]
"""
def somar_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

def somar_digitos_lista(lista_numeros):
    resultados = []
    for numero in lista_numeros:
        soma = somar_digitos(numero)
        resultados += [soma]
    return resultados

numeros = [10, 22, 345, 9]
somas_digitos = somar_digitos_lista(numeros)
print(somas_digitos)  