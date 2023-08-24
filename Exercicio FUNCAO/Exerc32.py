"""
Crie uma função que recebe uma lista de números e retorna uma nova lista com apenas
os números primos.
Exemplo de entrada: [1, 2, 3, 4, 5, 6]
Saída esperada: [2, 3, 5]
"""
def eh_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista_numeros):
    primos = [numero for numero in lista_numeros if eh_primo(numero)]
    return primos

numeros = [1, 2, 3, 4, 5, 6]
numeros_primos = filtrar_primos(numeros)
print(numeros_primos)  
