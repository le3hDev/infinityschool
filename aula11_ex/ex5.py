"""
5. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos:número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""
class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser maior que zero.")

    def consultarSaldo(self):
        return self.saldo

    def mostrarInformacoes(self):
        print(f"Conta Corrente - Número: {self.numero_conta}")
        print(f"Correntista: {self.nome_correntista}")
        print(f"Saldo: R${self.saldo:.2f}")

# Exemplo de uso da classe ContaCorrente
minha_conta = ContaCorrente("12345", "João da Silva")

minha_conta.mostrarInformacoes()
minha_conta.deposito(1000)
minha_conta.saque(500)
minha_conta.alterarNome("Maria Santos")

print("\nInformações da conta após operações:")
minha_conta.mostrarInformacoes()
