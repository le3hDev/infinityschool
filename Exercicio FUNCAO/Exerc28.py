"""
Escreva uma função que recebe uma lista de strings e retorna uma nova lista com as
strings invertidas.
Exemplo de entrada: ["python", "programação", "é", "divertida"]
Saída esperada: ["nohtyp", "ãçãçamargorp", "é", "aditrevid"]
"""
def inverter_strings(lista_strings):
    lista_invertida = [string[::-1] for string in lista_strings]
    return lista_invertida

strings = ["python", "programação", "é", "divertida"]
strings_invertidas = inverter_strings(strings)
print(strings_invertidas)  