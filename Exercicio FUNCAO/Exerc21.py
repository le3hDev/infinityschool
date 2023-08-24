"""
Faça uma função que recebe uma lista de strings e retorna a maior string.
Exemplo de entrada: ["python", "programação", "é", "divertida"]
Saída esperada: "programação"
"""
def encontrar_maior_string(lista_strings):
    maior_string = ""
    for string in lista_strings:
        if len(string) > len(maior_string):
            maior_string = string
    return maior_string

strings = ["python", "programação", "é", "divertida"]
maior_string_resultante = encontrar_maior_string(strings)
print(maior_string_resultante)  