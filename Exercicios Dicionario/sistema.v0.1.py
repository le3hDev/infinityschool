
itens =["celular", "Batedeira", "Televisao", "Notebook", "Aparelhos DVD"]

dicionario_precos = dict.fromkeys(itens)

valores =[1000,0,350.0, 2450.0, 6700.00, 200.0]

for i ,valor in enumerate(valores):
    dicionario_precos[itens[i]] = valor

print(dicionario_precos)


produto_desejado = input("Digite o nome do produto desejado: ")
preco = dicionario_precos.get(produto_desejado)
if preco is not None:
    print(f"O preço do {produto_desejado} é R${preco:.2f}")
else:
    print("Produto não encontrado.")
