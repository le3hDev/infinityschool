"""
Escreva uma função que recebe uma lista de strings 
e retorna a concatenação de todas elas.
Exemplo de entrada: ["Olá", "mundo", "!"]
Saída esperada: "Olá mundo!"
"""
def concatenar(lista):
    resultado = " "

    for string in lista:
        resultado += string
    return resultado


entradas = ["Ola"," ", "Mundo", "!"]
saida = concatenar(entradas)    
print(saida)