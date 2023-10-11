"""
3. Classe Retangulo: Crie uma classe que modele um retangulo:
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Area e calcular Perimetro;
c. Crie um programa que utilize esta classe.
Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""
class Retangulo:
    def __init__(self,comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura


    def mudarLados(self, novo_comprimento, nova_largura):
        self.comprimento = novo_comprimento
        self.largura = nova_largura

    def  retornarLados(self):
        return self.comprimento, self.largura
    
    def calcularAreas(self):
        return self.comprimento * self.largura
    
    def calcularPerimetro(self):
        return 2 * (self.comprimento * self.largura)
    

def calculaPisosERodaspes(local, piso_area, rodape_comprimento):
    area_local  = local.calcularAreas()
    quantidade_pisos = area_local / piso_area
    quantidade_rodapes = 2 * (local.comprimento + local.largura) / rodape_comprimento 
    return quantidade_pisos, quantidade_rodapes

comprimento = float(input('Informe o comprimento do local: '))
largura = float(input('Informe o largura do local: '))

local = Retangulo(comprimento,  largura)

piso_area = float(input(' Informe a area de cada piso: '))
rodape_comprimento = float(input(' Informe o comprimento de cada rodape: '))

quantidade_pisos,  quantidade_rodapes = calculaPisosERodaspes(local, piso_area, rodape_comprimento)

print('Quantidade de pisos necessarios:',quantidade_pisos)
print('Quantidade de rodapes necessarios: ',quantidade_rodapes)