from exibicao import mostrar_livros
from biblioteca import adicionar_livros,remover_livro

def main():

    LIVRO = {}

    while True:
        print(f"\n<<==== BIBLIOTECA ====>>\n")
        print(f"(1). Adicionar Livro.")
        print(f"(2). Remover Livro.")
        print(f"(3). Listar Livros.")
        print(f"(4). Sair.")

        opcao = int(input(f"\nInforme a operação que deseja realizar: "))

        if opcao == 1:

            titulo_livro = input(f"Informe o título: ")

            if titulo_livro in LIVRO:
                print(f"\n🟨| O título '{titulo_livro}' já está cadastrado na Biblioteca!")

            else:
                autor = input(f"Informe o nome do autor de '{titulo_livro}': ")
                adicionar_livros(LIVRO,titulo_livro,autor)
        
        elif opcao == 2:

            if len(LIVRO) <= 0:
                print(f"\nA Biblioteca está vazia.")

            else:
                titulo_livro = input(f"Informe o nome do livro que deseja remover da biblioteca: ")
                remover_livro(LIVRO,titulo_livro)
        
        elif opcao == 3:

            mostrar_livros(LIVRO)
        
        elif opcao == 4:
            print(f"Saindo da biblioteca. . . ")
            break

        else:
            print(f"Opção Inválida! Escolha uma opção de 1 à 4.")            

if __name__ == "__main__":
    main()

