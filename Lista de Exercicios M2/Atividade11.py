'''
Após, defina uma variável do tipo lista (list) e atribua a ela cinco
notas, sendo: 9.9, 10, 7.1, 7.8.
Em seguida, utilize o laço de repetição for para somar essas notas e, ao final,
exibir ao usuário a média simples.
Dica 1: a média simples é calculada a partir da soma dos valores divido pela quantidade desses valores.
Assim, se temos quatro notas, a média será: (nota1 + nota 2 + nota3 + nota4) / 4.
Dica 2: crie uma variável para que a soma seja armazenada. Assim, você utilizará o for apenas para somar. Ao
final, utilize a função print e exiba a média ao usuário.
'''

notas =[9.9, 10, 7.1, 7.8]
soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas) 
print(f"A média das notas é: {media:.2f}")




 