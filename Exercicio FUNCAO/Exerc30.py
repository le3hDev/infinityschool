"""
Faça uma função que recebe um número e retorna a sua raiz quadrada.
Exemplo de entrada: 9
Saída esperada: 3
"""
def calcular_raiz_quadrada(numero):
    raiz_quadrada =  int(numero ** 0.5)
    return raiz_quadrada

numero = 9
raiz_quadrada_resultante = calcular_raiz_quadrada(numero)
print(raiz_quadrada_resultante)  