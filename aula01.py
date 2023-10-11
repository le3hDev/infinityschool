class Pessoa:
    def __init__(self, nome:str, altura: float, idade: int):
        self.nome = nome
        self.altura = altura
        self.idade = idade

    #def mostrar_idade(self):
    #    print('A sua idade é: ', self.idade, 'anos')

    def mostrar_idade(self):
        return f'A sua idade é:  {self.idade} anos'    
    
    def fazer_aniversario(self):
        self.idade += 1

    def envelhecer(self, qnt_anos : int):
        self.idade += qnt_anos



pessoa_1 = Pessoa('Pedro', 1.72, 19)
pessoa_2 = Pessoa('Raimundo', 1.80, 42)

print(pessoa_1.mostrar_idade())
pessoa_1.envelhecer(10)
print(pessoa_1.mostrar_idade())



#pessoa_1.mostrar_idade()
#print(pessoa_1.mostrar_idade())
#pessoa_1.fazer_aniversario()
#print(pessoa_1.mostrar_idade())

#print(pessoa_2.mostrar_idade())
#pessoa_2.fazer_aniversario()
#print(pessoa_2.mostrar_idade())


