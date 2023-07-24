'''
Crie um programa que mostre na tela a soma de todos os números 
pares que estão no intervalo entre 1 e 50.
'''
soma = 0
for n in range(1, 51):
    if n % 2 == 0:
        soma += n
print(f'a soma dos numeros sao: {soma}')