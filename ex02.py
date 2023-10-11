class Carro:
    def __init__(self, nome: str, marca: str, ano: int, cor = 'preto'):
        self.nome = nome
        self.cor = cor
        self.marca = marca
        self.ano = ano


carro_1 = Carro('Fusca', 'Volkswagen', 1976 , 'azul')

print(vars(carro_1))