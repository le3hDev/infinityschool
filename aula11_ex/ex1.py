"""
1-  Classe Bola : Crie uma classe que modele uma bola:
    a. Atributos : Cor,  circunferencia  , material
    b. Métodos : trocarCor e mostrarCor
"""
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self, nova_cor):
        self.cor = nova_cor

    def mostrarCor(self):
        return self.cor

# Exemplo de uso da classe Bola
minha_bola = Bola("vermelha", 20, "plástico")
print("Cor da bola:", minha_bola.mostrarCor())

minha_bola.trocarCor("azul")
print("Nova cor da bola:", minha_bola.mostrarCor())
