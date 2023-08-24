"""
Crie uma função que recebe uma string e retorna a mesma string invertida.
Exemplo de entrada: "python"
Saída esperada: "nohtyp"
"""
def inverter_string(texto):
    tamanho = len(texto)
    string_invertida = " "
    for i in range(tamanho - 1,-1, -1):
        string_invertida += texto[i]
    return string_invertida

entrada = "python"
saida = inverter_string(entrada)
print (saida)    