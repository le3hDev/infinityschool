"""
A partir do exercício desenvolvido anteriormente, crie um arquivo Python exercicio29.py.
Após, remova todas as entradas da agenda.
Na sequência,utilize a função print para exibir o dicionário após a remoção dos valores.
Dica: utilize o método reservado para esse fim descrito na Tabela 1.
"""
agenda ={
    "Ana ": "321-231",
    "Paulo":"311-221",
    "Prata": "233-222",
    "Pedro": "100-223"
}
agenda.clear()
print(agenda.keys())