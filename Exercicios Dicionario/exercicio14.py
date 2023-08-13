"""
A partir do exercício desenvolvido anteriormente,crie um arquivo Python exercicio14.py.
Após, remova o item "item3" do estoque.
Dica: utilize o método reservado para esse fim descrito na Tabela 1.
"""
estoque ={
    "iphone":"10",
    "xiaomi":"5",
    "android":"20"
    }
estoque.popitem()
print(estoque.keys())