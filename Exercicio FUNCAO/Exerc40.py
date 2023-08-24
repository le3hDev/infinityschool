"""
Escreva uma função que recebe uma lista de strings e retorna a quantidade de palavras
que são palíndromos.
Exemplo de entrada: ["arara", "python", "ana", "radar"]
Saída esperada: 2
"""
def eh_palindromo(palavra):
    return palavra == palavra[::-1]

def contar_palindromos(lista_palavras):
    quantidade = 0
    for palavra in lista_palavras:
        if eh_palindromo(palavra):
            quantidade += 1
    return quantidade

palavras = ["arara", "python", "ana", "radar"]
quantidade_palindromos = contar_palindromos(palavras)
print(quantidade_palindromos)  # Deverá imprimir 2
