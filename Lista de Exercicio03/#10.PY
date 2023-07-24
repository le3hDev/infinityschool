'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. 
Não crie uma variável para cada ano de nascimento de cada pessoa.
'''
maiores_idade = 0
menores_idade = 0
ano_atual = 2023


for i in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano do nascimento da pessoa {i}° '))
    idade = ano_atual = ano_nascimento

    if idade >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1   
print(f'Quantidade de maiores idades: {maiores_idade}')
print(f'Quantidade de menoress idades: {menores_idade}')

