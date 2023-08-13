"""
A partir do exercício desenvolvido anteriormente,crie um arquivo Python exercicio10.py.
Após, imprima todas as chaves e valores do dicionário "pessoas" em pares.
"""
pessoas = {"nome":"Joao","idade":"25", "cidade":"bh"}
for chave, valor in pessoas.items():
    print(chave,'-',valor)