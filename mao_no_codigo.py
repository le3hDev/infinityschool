class Fatura:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

    def mostrar_itens(self):
        print(f'Nome: {self.nome}')
        print(f'Preço: {self.preço}')
        print(f'Quantidade: {self.quantidade}')

    def gerar_fatura(self):
        total = self.preço * self.quantidade
        return f'Total: {total}'
                   


fatura = Fatura('Camisa', 25,  10)
fatura_2 = Fatura('Calças', 150, 5)

fatura.mostrar_itens()
print(fatura.gerar_fatura())
fatura_2.mostrar_itens()
print(fatura_2.gerar_fatura())
