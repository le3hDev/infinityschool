"""
4. Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b. Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.altura += 0.5 * anos

    def engordar(self, peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def crescer(self, altura_ganha):
        self.altura += altura_ganha

    def mostrarInformacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} cm")

pessoa = Pessoa("Leandro", 18, 70, 170)

print("Informações iniciais:")
pessoa.mostrarInformacoes()

pessoa.envelhecer(2)
pessoa.engordar(5)
pessoa.crescer(1)
pessoa.emagrecer(3)

print("Informações após algumas mudanças:")
pessoa.mostrarInformacoes()
