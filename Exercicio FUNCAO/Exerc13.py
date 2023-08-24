"""
Escreva uma função que recebe uma lista de números e retorna a mediana.
Exemplo de entrada: [1, 2, 3, 4, 5]
Saída esperada: 3
"""
def calcular_mediana(lista_numeros):
    
    for i in range(len(lista_numeros)):
        for j in range(0, len(lista_numeros) - i - 1):
            if lista_numeros[j] > lista_numeros[j + 1]:
                lista_numeros[j], lista_numeros[j + 1] = lista_numeros[j + 1], lista_numeros[j]
    
    tamanho = len(lista_numeros)
    
    if tamanho % 2 == 1:
        mediana = lista_numeros[tamanho // 2]
    else:
       
        meio_superior = tamanho // 2
        meio_inferior = meio_superior - 1
        mediana = (lista_numeros[meio_inferior] + lista_numeros[meio_superior]) / 2
    
    return mediana

numeros = [1, 2, 3, 4, 5]
mediana_resultante = calcular_mediana(numeros)
print(mediana_resultante) 
