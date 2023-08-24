"""
Faça uma função que recebe uma lista de números 
e retorna a soma de todos os elementos
Exemplo de entrada: [1, 2, 3, 4]
Saída esperada: 10
"""
def somar_list(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma  

entrada = [1, 2, 3, 4]
resultado = somar_list(entrada)
print (resultado)