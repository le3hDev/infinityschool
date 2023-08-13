"""
A partir do exercício desenvolvido anteriormente,crie um arquivo Python exercicio20.py.
Após,verifique se o dicionário "frutas" está vazio.
"""
frutas = {
    "maça" : "6",
    "banana": "10",
    "laranja": "5"
}
frutas.update({"banana": "5",})
print(frutas.keys())