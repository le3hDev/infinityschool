'''
Faça um programa que conte de 1 até o número do usuário,
determine o menor valor, o maior valor e a soma dos valores. 
Faça que o programa receba apenas números entre 0 e 1000.
'''

n1 = int(input('Digite um numero entre  0 a 1000: '))
menor_valor = n1
maior_valor = 1
soma = 0

for num in range(1, n1 + 1):
    soma += num

    if num < menor_valor:
        menor_valor = num

    if num > maior_valor:
        maior_valor = num

print(f'Menor valor: {menor_valor}' )
print(f'Maior valor: {maior_valor}' )
print(f'Soma dos valor: {soma}' )
