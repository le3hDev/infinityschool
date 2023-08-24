"""
Faça uma função que recebe uma lista de números e retorna o menor valor.
Exemplo de entrada: [3, 8, 2, 5]
Saída esperada: 2
"""
def menor_valor(lista):
    if not lista:
        return None
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor


entrada =[3, 8, 2, 5]
saida = menor_valor(entrada)
print(saida)