def remover_cliente(lista):

    #Listar todos os clientes cadastrados
    print(f"\n<===== DESLIGAMENTO DE CLIENTES =====>\n")
    for i in range(len(lista)):
        print(f"{i + 1}º - {lista[i]}")

    #Coleta de dados do usuario (nome do cliente)
    nome_cliente = str(input(f"\nInforme o nome do cliente que deseja realizar o desligamento: "))

    #Verificando se a entrada do usuario (nome do cliente) está lista
    if nome_cliente in lista:

        #Se o nome do cliente estiver na lista
        lista.remove(nome_cliente)
        print(f"\nCliente Removido com Sucesso!")

    else:
        #Se o nome do cliente nao estiver na lista
        print(f"Cliente nao identificado e/ou inexistente.")

def adicionar_cliente(lista):

    #Colentando dados do usuario (nome do cliente)
    print(f"\n<========== CADASTRO ==========>")
    nome_cliente = str(input(f"Informe seu Nome Completo: "))

    #Guardando a informação do usuario dentro de uma lista
    lista.append(nome_cliente)

    print(f"\nCliente Adicionado com Sucesso!")

def listar_clientes(lista):

    print(f"\n<==== CLIENTES =====>\n")
    
    #Listar todos os clientes cadastrados
    for i in range(len(lista)):
        print(f"{i + 1}º - {lista[i]} ")

def main():

    CLIENTES = []

    #Menu com varias opções para o usuario selecionar a operação que deseja realizar
    
    while True:
        print(f"\n<< SISTEMA DE CADASTRO >>\n")
        print(f"1. Adicionar Cliente.")
        print(f"2. Remover Cliente.")
        print(f"3. Listar Clientes.")
        print(f"4. Finalizar Programa")
    
        opcao = int(input(f"\nInforme a operação que deseja realizar: "))
    
        if opcao == 1:
            adicionar_cliente(CLIENTES)
        
        elif opcao == 2:
            remover_cliente(CLIENTES)
        
        elif opcao == 3:
            listar_clientes(CLIENTES)
        
        elif opcao == 4:
            print(f"Finalizando . . .")
            break
        
        else:
            print(f"\nOpção inválida!")

if __name__ == "__main__":
    main()


    

