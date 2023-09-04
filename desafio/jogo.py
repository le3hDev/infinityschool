import random

def verificar_jogo(computador, jogador):
    if jogador == computador:
        resultado = "Empate"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        resultado = "Vitória"
    else:
        resultado = "Derrota"
    return resultado

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    if jogador in opcoes:
        resultado = verificar_jogo(computador, jogador)
        print(f"O computador escolheu {computador}.")
        print(f"Você escolheu {jogador}.")
        print(f"Resultado: {resultado}")
    else:
        print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")

jogar()
print("o jogo acabou")

    

