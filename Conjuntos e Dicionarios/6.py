def criar_eventos():
    
    obrigatorios = set()
    print("\n<== CADASTRO DE EVENTOS OBRIGATÓRIOS ==>\n")
    
    while True:
        evento = input("Digite o nome do evento obrigatório (ou 'sair' para finalizar): ")
        if evento.lower() == 'sair':
            break
        obrigatorios.add(evento)
    
    print("\nEventos obrigatórios cadastrados:", obrigatorios)
    return obrigatorios

def adicionar_eventos_realizados():
    realizados = set()
    print("\n<== ADICIONAR EVENTOS REALIZADOS ==>\n")
    
    while True:
        
        evento = input("Digite o evento que você realizou (ou 'sair' para finalizar): ").strip()
        if evento.lower() == 'sair':
            break

        realizados.add(evento)
    
    print("\nEventos realizados:", realizados)
    return realizados

def verificar_subconjunto(obrigatorios, realizados):
    return obrigatorios.issubset(realizados)

def main():
    obrigatorios = set()
    realizados = set()

    while True:
        print("\n<== MENU ==>\n")
        print("1. Criar eventos obrigatórios")
        print("2. Adicionar eventos realizados")
        print("3. Verificar se todos os eventos obrigatórios foram realizados")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            obrigatorios = criar_eventos()
        elif opcao == "2":
            realizados = adicionar_eventos_realizados()
        elif opcao == "3":
            if verificar_subconjunto(obrigatorios, realizados):
                print("\n Você realizou todos os eventos obrigatórios!")
            else:
                print("\n Ainda faltam eventos obrigatórios para serem concluídos.")
        elif opcao == "4":
            print("\nEncerrando o programa...")
            break
        else:
            print("\nOpção inválida! Escolha novamente.")

if __name__ == "__main__":
    main()
