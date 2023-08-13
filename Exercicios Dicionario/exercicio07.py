"""
A partir do exercício desenvolvido anteriormente,crie um arquivo Python exercicio07.py.
Após,atualize o valor correspondente à chave "idade" para um novo valor por meio da sobrescrita.
Na sequência,faça o mesmo procedimento com o método reservado para esse fim descrito nas Tabela 1.
"""
pessoas = {"nome":"Joao","idade":"25", "cidade":"bh"}
pessoas.update({"idade":"26"})
print(pessoas.get("idade"))
