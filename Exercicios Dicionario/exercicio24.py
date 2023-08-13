"""
A partir do exercício desenvolvido anteriormente,crie um arquivo Python exercicio24.py.
Após, remova o aluno com a nota mais baixa do dicionário "notas".
Dica 1: lembre dos exercícios anteriores e de como fizemos para calcular somar itens a partir do laço de
repetição for.
É desejável o uso do laço para resolução desse exercício.
Dica 2: utilize o método reservado para esse fim descrito na Tabela 1.
"""
notas ={
  
     "Alice": "8",
    "Bob": "7",
    "Carol": "9",
    "David": "6",
    "Eve": "5"
}
aluno_mais_baixo = None
nota_mais_baixa = "5"

for aluno, nota in notas.items():
    if nota <= nota_mais_baixa:
        aluno_mais_baixo = aluno
        nota_mais_baixa = nota
    if aluno_mais_baixo:
        print(f"O aluno com a nota mais baixa é {aluno_mais_baixo} com a nota {nota_mais_baixa}.")
    else:
        print("Nenhum aluno encontrado no dicionário de notas.")