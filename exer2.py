''''
Crie um programa que leia dois valores e mostre um  menu na tela:
[1] somar
[2] multplicar
[3] maior
[4] novos numeros
[5] sair do programa

'''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

while True:
        print("\n----- Menu -----")
        print("[1] Somar")
        print("[2] Multiplicar")
        print("[3] Maior")
        print("[4] Novos números")
        print("[5] Sair do programa")

        opcao = input("Escolha uma opção (1, 2, 3, 4 ou 5): ")

        if opcao == '1':
            print(f"A soma de {numero1} + {numero2} é: {numero1 + numero2}")
        elif opcao == '2':
            print(f"A multiplicação de {numero1} * {numero2} é: {numero1 * numero2}")
        elif opcao == '3':
            print(f"O maior número entre {numero1} e {numero2} é: {max(numero1, numero2)}")
        elif opcao == '4':
            numero1 = float(input("Digite o novo primeiro número: "))
            numero2 = float(input("Digite o novo segundo número: "))
        elif opcao == '5':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção válida (1, 2, 3, 4 ou 5).")




                     







