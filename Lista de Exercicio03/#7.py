'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
primeiro_termo = int(input(" Digite o primero termo da PA: "))
razao = int(input("Digite a razao da PA: "))

print("Os 10 primeiros termos da PA sao: ")
for i in range(10):
    termo_atual = primeiro_termo + i * razao
    print(termo_atual, end = " ")
