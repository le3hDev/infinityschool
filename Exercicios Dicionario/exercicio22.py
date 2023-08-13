"""
A partir do exercício desenvolvido anteriormente,crie um arquivo Python exercicio22.py.
Após, calcule a média das notas dos alunos.
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

soma_notas = 0
for nota in notas.values():
    soma_notas += nota

media_notas = soma_notas / len(notas)

print(f"A média das notas dos alunos é: {media_notas}")