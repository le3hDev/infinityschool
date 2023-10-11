"""
Crie uma classe chamada Cachorro que possua 3 atributos: nome, raça e peso. Implemente um método: comer ração, que retorna "croc croc croc". 
"""
class Cachorro():
    def __init__(self,nome,raça, peso):
        self.nome = nome
        self.raça = raça
        self.peso = peso

    def comer(self):
        print(f'{self.nome} :croc croc croc' )   