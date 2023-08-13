"""
A partir do exercício desenvolvido anteriormente,crie um arquivo Python exercicio06.py.
Após,remova a entrada com a chave "cidade" do dicionário "pessoas".
"""
pessoas = {"nome":"Joao","idade":"25", "cidade":"bh"}
pessoas.popitem()
print(pessoas.keys());