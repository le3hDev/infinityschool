"""
A partir do exercício desenvolvido anteriormente,crie um arquivo Python exercicio19.py.
Após, caso a chave "banana" não exista, crie a chave e atribua a ela um valor qualquer.Na sequência, incremente seu valor em uma quantidade.
Dica 1: crie a chave "banana" e atribua a ela o valor 5, caso não exista no dicionário. Dica 2: caso já tenha
definida a chave "banana", experimente utilizar o método descrito na Tabela 1 para solução do problema.
"""
frutas = {
    "maça" : "6",
    "banana": "10",
    "laranja": "5"
}
frutas.update({"banana": "5",})
print("Valor da chave 'banana':", frutas["banana"])