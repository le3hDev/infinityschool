'''
Repita os procedimentos da atividade anterior em um arquivo Python atividade14.py.
Dessa vez, utilize o algoritmo anterior para contar a quantidade de consoantes.
'''
palavra = input('Digite uma  palavra:')
quantidade = 0
for letras in palavra:
        if letras == 'b' or letras == 'c' or letras == 'd' or letras == 'f' or letras == 'g':
            quantidade += 1
print(f"A palavra {palavra} tem {quantidade} , consoantes.")
