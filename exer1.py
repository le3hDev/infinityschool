"""
Faca um programa que leia 5 numeros e infomer o maior numero.
"""

quero_ler = 5
c = 0
maior = 0
while c < quero_ler:
    n = int(input("Digite um numero:"))
    if n > maior:
        maior = n
    else:
        if n > maior:
            maior = n
    c += 1
    print(f"MAIOR: {maior}")
print("fim")        
