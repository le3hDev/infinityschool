"""
Escreva uma função que recebe dois numeros como argumentos e retorna sua soma.
Exemplo de entrada :2,3
Saida esperada: 5
"""
def somar(n1 , n2):
    soma = n1 + n2
    print(soma)

n1 =int(input("Digite um numero: "))
n2 =int(input("Digite um numero: "))
somar(n1, n2)