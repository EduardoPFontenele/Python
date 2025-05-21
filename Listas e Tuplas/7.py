def adicionar_filmes(lista):

    #Coletando dados do usuario (nome de um filme)
    nome_filme = str(input(f"Informe o nome do filme assistido: "))
    
    #Armazenando a informação em uma lista
    lista.append(nome_filme)

    print(f"-" * 30)
    print(f"Filme Adicionado à Lista!")
    print(f"-" * 30)
    
def mostrar_filmes(lista):

    #Mostrando os ultimos 3 dados da lista
    tres_ultimos_filmes = lista[len(lista) - 3:len(lista):1]
    print(f"-> {tres_ultimos_filmes}")

def remover_filme(lista):

    print(f"\n<< FILMES >>\n")
    #Listar as informações da lista
    for i in range(len(lista)):
        print(f"({i + 1}). {lista[i]}")

    #Coletando informações do usuario
    nome_filme = str(input(f"\nDigite o nome do filme que deseja remover da lista: "))

    #Verificando o dado do usuario com o elemento da lista
    if nome_filme in lista:

        #Remover um item da lista
        lista.remove(nome_filme)
    
    print(f"-" * 30)
    print(f"Filme removido da lista.")
    print(f"-" * 30)

def main():
    
    FILMES = []

    while True:
        #Menu com varias opções para o usuario selecionar a operação que deseja realizar
        print(f"\n<< CONTROLE DE FILMES ASSISTIDOS >>\n")
        print(f"1. Adicionar Filme.")
        print(f"2. Mostrar Filmes Assistidos Recentemente.")
        print(f"3. Remover Filme.")
        print(f"4. Encerrar Programa.")

        opcao = int(input(f"\nInforme a operação que deseja realizar: "))

        if opcao == 1:
            print(f"")
            adicionar_filmes(FILMES)
        
        elif opcao == 2:
            print(f"\n<< FILMES ASSISTIDOS RECENTEMENTE >>\n")
            mostrar_filmes(FILMES)
        
        elif opcao == 3:
            remover_filme(FILMES)
        
        elif opcao == 4:
            print(f"Finalizando . . .")
            break
        
        else:
            print(f"Opção Invalida!")

if __name__ == "__main__":
    main()