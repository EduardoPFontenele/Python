def cadastrar_usuario(nome_arquivo, nome_usuario, senha, permissao):
    if not nome_usuario.strip() or not senha.strip():
        print("\n❗ Nome de usuário e senha não podem estar vazios!")
        return

    try:
        # Abrindo o arquivo 'dados' no modo de leitura
        with open(nome_arquivo, 'r', encoding='utf-8-sig') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')

                # Verificando se o nome de usuário já existe no sistema
                if len(dados) > 0 and dados[0].strip().lower() == nome_usuario.strip().lower():
                    print(f"\n❌ Já existe um usuário com este nome!")
                    print("🏃 Retornando ao Menu Principal . . .")
                    return
                
    except FileNotFoundError:
        pass  # Arquivo não existe, então nenhum usuário está cadastrado ainda

    # Caso o usuário não tenha sido cadastrado
    with open(nome_arquivo, "a", encoding='utf-8-sig') as arquivo:
        # Se o usuário for administrador
        if permissao == 's':
            arquivo.write(f"{nome_usuario},{senha},Administrador\n")
        # Se o usuário for um usuário casual
        elif permissao == 'n':
            arquivo.write(f"{nome_usuario},{senha},0\n")

        print(f"\n✅ Usuário Cadastrado com sucesso!")
    print("🏃 Retornando ao Menu Principal . . .")