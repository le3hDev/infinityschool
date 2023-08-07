'''
Após, defina uma variável do tipo lista (list) e atribua a ela cinco notas, sendo: 9.9, 10, 7.1, 7.8.
Em seguida, utilize o laço de repetição for para somar essas notas e, ao final, exibir ao usuário a média ponderada. Considere os seguintes
pesos para cada nota, respectivamente: 4, 2, 3, 1.

'''
notas = [9.9, 10, 7.1, 7.8]
pesos = [4, 2, 3, 1]
soma_ponderada = 0


for i in range(len(notas)):
    soma_ponderada += notas[i] * pesos[i]

media_ponderada = soma_ponderada / sum(pesos)
print("A média ponderada das notas é:", media_ponderada)

