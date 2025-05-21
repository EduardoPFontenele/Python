def adicionar_produtos(produtos,precos):

    #Coleta de informações do usuario
    produto = str(input(f"Informe o produto que deseja adicionar ao carrinho: "))
    preco = float(input(f"Informe o preço do produto (R$): "))

    #Verificação de erro caso o preço informado for menor que 0
    if preco < 0:
        print(f"\nValor de preço inválido!")

    else:
        #Armazenando os dados dos usuarios em duas diferentes listas
        produtos.append(produto)
        precos.append(preco)

        print(f"-" * 30)
        print(f"\nProduto adicionado ao carrinho!")
        print(f"-" * 30)

def exibir_lista_de_compras(produtos,precos):

    print(f"\n<< PRODUTOS DO CARRINHO >>\n")

    print(f"-" * 30)
    
    #Laço para percorrer a lista 'produtos' e lista 'preços',monstrando os elementos de cada lista
    for i in range(len(produtos)):
        print(f"{produtos[i]} - R$ {precos[i]}")

    print(f"-" * 30)

def calcular_compra(precos):

    #Somar todas as informações da lista 'precos'
    total_compra = sum(precos)
    print(f"-" * 30)
    print(f"PREÇO DO CARRINHO = R${total_compra:.2f}")
    print(f"-" * 30)

def remover_produto(produtos,precos):

    print(f"\n<< REMOVER PRODUTOS DO CARRINHO >>\n")

    #Laço para listar os elementos da lista 'produtos' e lista 'precos'
    for i in range(len(produtos)):
        print(f"({i+1}). {produtos[i]} - R$ {precos[i]}")

    #Coletando dados do usuario
    nome_produto = str(input(f"\nInforme o nome do produto que deseja remover do carrinho: "))

    #Excluindo itens da lista 'preco' e lista 'produto' dada a informação do usuario
    if nome_produto in produtos:
        indice = produtos.index(nome_produto)

        del produtos[indice]
        del precos[indice]
    
    print(f"-" * 30)
    print(f"Produto removido do carrinho!")
    print(f"-" * 30)

def main():

    PRODUTOS = []
    PRECOS = []

    while True:
        #Menu com varias opções para o usuario selecionar a operação que deseja realizar
        print(f"\n<< CARRINHO DE COMPRAS >>\n")
        print(f"1. Adicionar Produto.")
        print(f"2. Exibir Produtos do Carrinho.")
        print(f"3. Preço Total do Carrinho.")
        print(f"4. Remover Item do Carrinho.")
        print(f"5. Encerrar Programa.")

        opcao = int(input(f"\nInforme a operação que deseja realizar: "))

        if opcao == 1:
            adicionar_produtos(PRODUTOS,PRECOS)
        
        elif opcao == 2:
            exibir_lista_de_compras(PRODUTOS,PRECOS)
        
        elif opcao == 3:
            calcular_compra(PRECOS)

        elif opcao == 4:
            remover_produto(PRODUTOS,PRECOS)
        
        elif opcao == 5:
            print(f"Finalizando . . .")
            break
        
        else:
            print(f"Opção Inválida")
    
if __name__ == "__main__":
    main()