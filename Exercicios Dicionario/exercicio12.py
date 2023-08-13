"""
A partir do exercício desenvolvido anteriormente,crie um arquivo Python exercicio12.py.
Após, calcule o total de itens no estoque.
"""
estoque ={
    "iphone":"10",
    "xiaomi":"5",
    "android":"20"
    }
total_items = len(estoque.values())

print(" Total de itens no estoque :" , total_items)