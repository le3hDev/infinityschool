"""
Faça uma função que recebe uma lista de números e retorna o fatorial de cada número.
Exemplo de entrada: [4, 5, 6]
Saída esperada: [24, 120, 720]
"""
def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def calcular_fatorial_lista(lista_numeros):
    fatoriais = [calcular_fatorial(numero) for numero in lista_numeros]
    return fatoriais

numeros = [4, 5, 6]
fatoriais = calcular_fatorial_lista(numeros)
print(fatoriais)  
