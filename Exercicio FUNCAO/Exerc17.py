"""
Crie uma função que recebe uma string e retorna a quantidade de vogais presentes nela.
Exemplo de entrada: "python"
Saída esperada: 2
"""
def contar_vogais(texto):
    vogais = "AEIOUaeiou"
    quantidade = 1
    
    
    for letra in texto:
        if letra in vogais:
            quantidade += 1
    
    return quantidade

entrada = "python"
quantidade_vogais = contar_vogais(entrada)
print(quantidade_vogais)  
