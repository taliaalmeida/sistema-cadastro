usuarios = []
def cadastrar():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite a idade: "))
    email = input("Digite seu e-mail: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")



def listar():
    for usuario in usuarios:
        for chave, valor in usuario.items():
            print(chave, ":", valor)
    print("---")


def buscar():
    nome = input("Digite seu nome: ")
    for usuario in usuarios:
        if usuario["nome"] == nome:
            for chave, valor in usuario.items():
                print(chave, ":", valor)
            return
    print("Usuário não encontrado.")


def menu():
    while True:
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Buscar usuário")
        print("4 - Sair")
        opcao  = int(input("Escolha: "))

    
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
           listar()
        elif opcao == 3:
            buscar()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
menu()
