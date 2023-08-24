"""
Faça uma função que recebe uma lista de números e retorna uma nova lista com apenas
os números ímpares.
Exemplo de entrada: [1, 2, 3, 4, 5, 6]
Saída esperada: [1, 3, 5]
"""
def numeros_impares(lista_numeros):
   lista_impares = [numero for numero in lista_numeros if numero %2 != 0]
   return lista_impares


entrada = [1, 2, 3, 4, 5, 6]
saida = numeros_impares(entrada)
print(saida)