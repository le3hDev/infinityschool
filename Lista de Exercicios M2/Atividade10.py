'''
Crie um arquivo Python atividade10.py. Após, defina uma variável do tipo lista (list) e atribua a ela cinco
palavras, sendo: "limão", "laranja", "maracujá", "abacaxi" e "mexerica".
Depois, peça ao usuário que informe uma fruta, e atribua o valor lido a uma variável fruta. 
Finalmente, utilize a condicional if e verifique se a fruta
informada pelo usuário faz parte da lista de frutas que você definiu anteriormente. Se verdadeiro, exiba o
nome da fruta; caso contrário, informe ao usuário:
'''

lista = ["limão", "laranja", "maracujá", "abacaxi", "mexerica"]
fruta = input("Digite a fruta: ")

if fruta in lista:
    print(fruta)
else:
    print("Fruta não encontrada")    