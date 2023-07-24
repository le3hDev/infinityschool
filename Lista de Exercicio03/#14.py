'''
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''
numero_eleitores = int(input("Digite o número total de eleitores: "))

votos_candidatos = [0, 0, 0]

for eleitor in range(1, numero_eleitores + 1):
    print(f"Eleitor {eleitor}:")
    voto = int(input("Digite o número do candidato (1, 2 ou 3): "))
    
    while voto not in (1, 2, 3):
        print("Voto inválido. Digite '1', '2' ou '3'.")
        voto = int(input("Digite o número do candidato (1, 2 ou 3): "))
    
    votos_candidatos[voto - 1] += 1

print("Resultado da eleição:")
print(f"Candidato 1: {votos_candidatos[0]} voto(s)")
print(f"Candidato 2: {votos_candidatos[1]} voto(s)")
print(f"Candidato 3: {votos_candidatos[2]} voto(s)")
