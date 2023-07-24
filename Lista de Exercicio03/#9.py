'''
Crie um programa que leia uma frase qualquer 
e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, 
A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''
frase = int(input('Digite uma frase:'))
eh_palindromo = True
for i in range(frase) // 2:
    if frase[i] != frase[ - (i + 1)]:
        eh_palindromo = False
        break


if eh_palindromo:
    print ('A frase é um palindromo.')
else:
    print ('A frase nao é um palindromo.')
