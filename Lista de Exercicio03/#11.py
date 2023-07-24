'''
Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
Utilize for sem criar uma variável para o peso de cada uma das pessoas.
'''

maior_peso = 0
menor_peso = 0

for i in range(1, 6):
    peso = float(input(f'Digite o peso da pessoa:{i} '))
    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print(f'Maior peso lido: {maior_peso:.2f} Kg')     
print(f'Menor peso lido: {menor_peso:.2f} Kg')     
