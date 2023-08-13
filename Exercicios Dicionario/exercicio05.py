"""
A partir do exercício desenvolvido anteriormente, crie um arquivo Python exercicio05.py.
Após,verifique se a chave "altura" existe no dicionário "pessoas".
"""
pessoas = {"nome":"Joao","idade":"25", "cidade":"bh"}
for chave, valor in pessoas.items():
    print(chave,valor)