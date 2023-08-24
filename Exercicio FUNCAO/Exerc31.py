"""
Escreva uma função que recebe um número e verifica se é um número perfeito.
Exemplo de entrada: 6
Saída esperada: True
"""
def eh_numero_perfeito(numero):
    if numero <= 0:
        return False  
    
    soma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    
    return soma_divisores == numero

numero = 6
resultado = eh_numero_perfeito(numero)
print(resultado) 