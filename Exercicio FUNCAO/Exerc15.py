"""
Faça uma função que recebe um número e retorna a sequência de Fibonacci até esse
número.
Exemplo de entrada: 8
Saída esperada: [0, 1, 1, 2, 3, 5, 8]
"""
def fibonacci_ate(numero):
    fibonacci = [0, 1]
    
    while fibonacci[-1] + fibonacci[-2] <= numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    return fibonacci

numero = 8
sequencia_fibonacci = fibonacci_ate(numero)
print(sequencia_fibonacci)  