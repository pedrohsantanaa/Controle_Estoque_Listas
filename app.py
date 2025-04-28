import os

produtos = []

def cadastrar():
    os.system("cls")
    produto = str(input("Informe o nome do produto:"))
    produtos.append(produto)
    print(f"Produto {produto} cadastrado")

def listar():
    os.system("cls")
    for i in enumerate(produtos):
        print(i)

def excluir():
    os.system("cls")
    listar()

    codigo = int(input("Digite o número do produto a excluir:"))
    produtos.pop(codigo)

    print("Produto Excluido com Sucesso!!")
    listar()

while True:
    print("\n\n\n")
    print("Sabor Tocantinense")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Excluir Produtos")
    print("4 - Sair")

    opcao = int(input("Digite uma opção:"))

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        excluir()
    elif opcao == 4:
        print("Saindo do sistema...")
        break
    else:
        print("Opção Não Econtrada")






# cont = 0
# while cont < 5:
#     print("Volta:",cont)
#     cont = cont + 1

# for i in range(10):
#     print(i)