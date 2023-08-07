''''
Crie um arquivo Python atividade13.py.
Após, peça que o usuário informe uma palavra qualquer e armazene o valor lido em uma variável.
Na sequência, utilize o laço for para verificar quantas vogais têm na palavra em questão.
Ao final, exiba ao usuário a seguinte mensagem: print(f"A palavra {palavra} tem {quantidade}
vogais.")
'''
palavra = input('Digite uma  palavra:')
quantidade = 0
for letras in palavra:
    if letras == 'a' or letras == 'e' or letras == 'i' or letras == 'o' or letras == 'u':
        quantidade += 1
print(f"A palavra {palavra} tem {quantidade} vogais.")
