def adicionar_produto(nome,preco,quantidade,dicionario):

    produtos = {

        "Nome": nome,
        "Preco": preco,
        "Quantidade": quantidade
    }

    dicionario[nome] = produtos
    print(f"\nProduto '{nome}' cadastrado com sucesso!")

def modificar_preco(dicionario,nome_produto):

    if nome_produto in dicionario:
        preco_atualizado = float(input(f"Informe o preço atualizado de {nome_produto}: "))

        dicionario[nome_produto]["Preco"] = preco_atualizado

        print(f"\n{dicionario}")
        print(f"\nPreço de '{nome_produto}'atualizado!")

    else:
        print(f"Produto Inexistente!")

def modificar_quantidade(dicionario,nome_produto):

    if nome_produto in dicionario:
        quantidade_atualizada = int(input(f"Informe a quantidade atualizade de {nome_produto}: "))
        dicionario[nome_produto]['Quantidade'] = quantidade_atualizada

        print(f"\n{dicionario}")
        print(f"\nQuantidade de {nome_produto} atualizada!")
    
    else:
        print(f"Produto Inexistente!")

def remover_produto(dicionario,nome_produto):

    if nome_produto in dicionario:
        del dicionario[nome_produto]

    print(f"Produto '{nome_produto}' removido!")

def main():

    PRODUTOS = {}

    while True:
        print(f"\n<===== CADASTRO DE PRODUTOS =====>\n")
        print(f"1. Adicionar novo produto.")
        print(f"2. Modificar preço.")
        print(f"3. Modificar quantidade.")
        print(f"4. Remover produto.")
        print(f"5. Encerrar programa.")

        opcao = int(input(f"\nQual operação deseja realizar: "))

        if opcao == 1:

            nome = str(input(f"Informe o nome do produto: "))
            preco = float(input(f"Informe o preço do produto: R$ "))
            quantidade = int(input(f"Informe a quantidade de produtos: "))

            adicionar_produto(nome,preco,quantidade,PRODUTOS)
        
        elif opcao == 2:
            nome_produto = str(input(f"Qual o produto deseja modificar o preço: "))
            modificar_preco(PRODUTOS,nome_produto)
        
        elif opcao == 3:
            nome_produto = str(input(f"Qual o produto deseja modificar o preço: "))
            modificar_quantidade(PRODUTOS,nome_produto)
        
        elif opcao == 4:
            nome_produto = str(input(f"Qual produto deseja remover: "))
            remover_produto(PRODUTOS,nome_produto)
            
        elif opcao == 5:
            print(f"Finalizando . . .")
            break

        else:
            print(f"Opção Invalida")

if __name__ == "__main__":
    main()

