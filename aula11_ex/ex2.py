"""
2 - Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Area;
"""
class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mudarLado(self, novo_tamanho):
        self.tamanho_do_lado = novo_tamanho

    def retornarLado(self):
        return self.tamanho_do_lado

    def calcularArea(self):
        return self.tamanho_do_lado ** 2


meu_quadrado = Quadrado(6)
print("Tamanho do lado:", meu_quadrado.retornarLado())
print("Área do quadrado:", meu_quadrado.calcularArea())

meu_quadrado.mudarLado(9)
print("Novo tamanho do lado:", meu_quadrado.retornarLado())
print("Nova área do quadrado:", meu_quadrado.calcularArea())
