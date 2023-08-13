"""
A partir do exercício desenvolvido anteriormente,crie um arquivo Python exercicio23.py.
Após, encontre o aluno com a nota mais alta no dicionário "notas".
Dica: lembre dos exercícios anteriores e de como fizemos para calcular somar itens a partir do laço de
repetição for.
É desejável o uso do laço para resolução desse exercício.
"""
notas = {
    "Alice": "8",
    "Bob": "7",
    "Carol": "9",
    "David": "6",
    "Eve": "5"
}
aluno_mais_alto = None
nota_mais_alta = "-1"

for aluno, nota in notas.items():
    if nota > nota_mais_alta:
        aluno_mais_alto = aluno
        nota_mais_alta = nota
    if aluno_mais_alto:
        print(f"O aluno com a nota mais alta é {aluno_mais_alto} com a nota {nota_mais_alta}.")
    else:
        print("Nenhum aluno encontrado no dicionário de notas.")
