from biblioteca import Biblioteca
from livro import Livro
from revista import Revista


def menu():
    print("\n===== SISTEMA BIBLIOTECA =====")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Revista")
    print("3. Listar Itens")
    print("4. Emprestar Item")
    print("5. Devolver Item")
    print("6. Sair")


biblioteca = Biblioteca()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = input("Código: ")
        titulo = input("Título: ")
        ano = int(input("Ano: "))
        autor = input("Autor: ")
        paginas = int(input("Número de páginas: "))
        livro = Livro(codigo, titulo, ano, autor, paginas)
        biblioteca.adicionar_item(livro)

    elif opcao == "2":
        codigo = input("Código: ")
        titulo = input("Título: ")
        ano = int(input("Ano: "))
        edicao = int(input("Edição: "))
        mes = input("Mês: ")
        revista = Revista(codigo, titulo, ano, edicao, mes)
        biblioteca.adicionar_item(revista)

    elif opcao == "3":
        biblioteca.listar_itens()

    elif opcao == "4":
        codigo = input("Código do item: ")
        biblioteca.emprestar_item(codigo)

    elif opcao == "5":
        codigo = input("Código do item: ")
        biblioteca.devolver_item(codigo)

    elif opcao == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")