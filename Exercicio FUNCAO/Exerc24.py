"""
Faça uma função que recebe uma lista de strings e retorna uma nova lista com as strings
em ordem alfabética.
Exemplo de entrada: ["python", "programação", "é", "divertida"]
Saída esperada: ["divertida", "programação", "python", "é"]
"""
def ordenar_alfabeticamente(lista_strings):
    for i in range(len(lista_strings)):
        for j in range(0, len(lista_strings) - i - 1):
            if lista_strings[j] > lista_strings[j + 1]:
                lista_strings[j], lista_strings[j + 1] = lista_strings[j + 1], lista_strings[j]
    return lista_strings

strings = ["python", "programação", "é", "divertida"]
strings_ordenadas = ordenar_alfabeticamente(strings)
print(strings_ordenadas) 