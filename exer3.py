''''
Faça um programa que leia  um numero qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
if __name__ == "__main__":
    numero = int(input("Digite um número para calcular o fatorial: "))
    fatorial = 1

    while numero > 1: 
        fatorial *= numero
        numero -= 1

    print(f"Fatorial = {fatorial}")

