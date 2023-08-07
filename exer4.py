''''
Faca um programa que leia um nome de usua
 e a sua senha e nao aceite a senha igual ao nome do usuario, mostre a msg de erro e volte a pedir as informacoes.


 '''
controle = True

# 1 sinal de  = é de recebe.
# 2 é  == verificacao.

while controle == True:
        nome_usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
    
        if nome_usuario == senha:
            print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
            print("So Aceite  senha de  4 Digitos")

        elif len(senha)< 4:
             print("Erro: A senha não pode ser Cadastrada, Tente novamente.")
        else:
            print("Usuário e senha cadastrados com sucesso!")
            
            controle = False
     