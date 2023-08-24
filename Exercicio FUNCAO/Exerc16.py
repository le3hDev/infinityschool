"""
números repetidos.
Exemplo de entrada: [1, 2, 3, 3, 4, 4, 5]
Saída esperada: [1, 2, 3, 4, 5]
"""
def remover_repetidos(lista):
    lista_sem_repeticao = []
    for numero in lista:
        encontrado = False
        for num_sem_repeticao in lista_sem_repeticao:
            if num_sem_repeticao == numero:
                encontrado = True
                break
        if encontrado == False:
            lista_sem_repeticao.append(numero)
    return lista_sem_repeticao

entrada = [1, 2, 3, 3, 4, 4, 5]
lista_sem_repeticao = remover_repetidos(entrada)
print(lista_sem_repeticao)  