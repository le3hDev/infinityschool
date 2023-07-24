'''
Desenvolva um programa que leia seis números inteiros 
e mostre a soma apenas daqueles que forem pares e quantos números pares foram informados. Se o valor digitado for ímpar, desconsidere-o na soma. Não crie uma variável para cada número nesse exercício.
'''
soma_pares = 0
quantidade_pares = 0

for i in range(6):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1

print(f"A soma dos números pares é: {soma_pares}")
print(f"Quantidade de números pares informados: {quantidade_pares}")

      

