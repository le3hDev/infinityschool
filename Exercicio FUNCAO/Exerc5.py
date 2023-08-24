"""
Crie uma função que recebe uma lista de números e retorna o maior valor.
Exemplo de entrada: [3, 8, 2, 5]
Saída esperada: 8
"""
def maior_valor(lista):
    if not lista:
        return None
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior


entrada =[3, 8, 2, 5]
saida = maior_valor(entrada)
print(saida)

