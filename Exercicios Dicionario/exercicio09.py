"""
A partir do exercício desenvolvido anteriormente, crie um arquivo Python exercicio09.py.
Após, imprima todos os valores do dicionário "pessoas".
Dica 1: utilize o laço de repetição for para execução dessa tarefa.
Dica 2: utilize o método reservado para esse fim descrito na Tabela 1.
"""
pessoas = {"nome":"Joao","idade":"25", "cidade":"bh"}
pessoas.update({"idade":"26"})

for chave,valor in pessoas.items():
    print(valor)