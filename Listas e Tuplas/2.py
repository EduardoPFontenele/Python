def informar_produtos(lista,quantidades):

    #Laco para coletar informações de um usuario
    for i in range(5):

        #Coleta de dados do usuario(Nome do produto)
        produto = str(input(f"\nInforme o nome do {i + 1}º produto do estoque: "))

        #Armazenando o 'nome do produto' em uma lista
        lista.append(produto)

        #Coleta de dados do usuario (quantidade do produto informado)
        quantidade = int(input(f"Informe a quantidade de {lista[i]} no estoque: "))

        #Verificacao de erro caso a quantidade informada seja menor que 0
        if quantidade < 0:
            print(f"\nValor invalido")
            break
        else:
            #Armazena a 'quantidade dos produtos' em uma lista
            quantidades.append(quantidade)
        print(f"-" * 30)
        print(f"Produto Cadastrado com Sucesso!")
        print(f"-" * 30)

def consultar_estoque(nomes,quantidades):

    #Laço para listar o nome de todos os 'produtos' cadastrados
    for i in range(len(nomes)):
        print(f"{i + 1}. {nomes[i]}")

    #Coleta de dados do usuario (nome do produto)
    nome_produto = input("\nInforme o nome do produto que deseja consultar no estoque: ")

    #Buscando a posicao da lista do produto informado pelo usuario
    for produto in nomes:
        if nome_produto == produto:
            indice = nomes.index(nome_produto)
    
    print(f"-" * 30)
    print(f"Quantidade de {nome_produto} = {quantidades[indice]}")
    print(f"-" * 30)
    
def main():

    PRODUTOS = []
    QUANTIDADE_PRODUTOS = []

    #Menu com varias opções para o usuario selecionar a operação que deseja realizar
    while True:
        print(f"\n<< CONTROLE DE ESTOQUE >>\n")
        print(f"1. Adicionar 5 Produtos ao Estoque.")
        print(f"2. Consultar Estoque.")
        print(f"3. Finalizar Programa")

        opcao = int(input(f"\nInforme a operação que deseja realizar: "))

        if opcao == 1:
            print(f"\n<< ADICIONAR AO ESTOQUE >>")
            informar_produtos(PRODUTOS,QUANTIDADE_PRODUTOS)

        elif opcao == 2:
            print(f"\n<< ESTOQUE >>\n")
            consultar_estoque(PRODUTOS,QUANTIDADE_PRODUTOS)
        
        elif opcao == 3:
            print(f"Finalizando . . .")
            break  

        else:
            print(f"\nOpção Inválida!")

if __name__ == "__main__":
    main()