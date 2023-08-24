"""
Faça uma função que recebe uma lista de números e retorna a média deles.
Exemplo de entrada: [4, 5, 6, 7]
Saída esperada: 5.5
"""
def  media (lista_num):
    if len(lista_num) == 0:
        return  0
    

    soma  = 0
    for numero in lista_num:
        soma += numero
    media = soma / len(lista_num)
    return media

numeros = [4, 5,  6, 7]
media_result = media(numeros)
print (media_result)