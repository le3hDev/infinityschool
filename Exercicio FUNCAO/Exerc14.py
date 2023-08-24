"""
Crie uma função que recebe um número e verifica se é primo.
Exemplo de entrada: 7
Saída esperada: True
"""

def numero_primo (numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
        
    return True    
        
numero = 7
resultado = numero_primo(numero)
print (resultado)        