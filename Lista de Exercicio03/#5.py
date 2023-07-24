'''
Refaça o exercício da tabuada de um número
que o usuário escolher, só que agora utilizando um laço for
'''
numero = int(input('Digite um numero: '))
for n in range(1, 11):
    resultado = numero * n
    print(f'{numero} x {n} = {resultado}')
