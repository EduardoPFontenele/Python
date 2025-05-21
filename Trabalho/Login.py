from Menu_Administrador import menu_administrador
from Menu_Usuario import menu_casual

def logar_na_conta(nome_arquivo, nome_usuario, senha_informada, DADOS):

    # Verificação caso o input do usuário seja vazio
    if not nome_usuario.strip() or not senha_informada.strip():
        print("\n❗ Nome de usuário e senha não podem estar vazios!")
        return

    try:
        # Abrindo o arquivo 'dados.txt' no modo de leitura
        with open(nome_arquivo, 'r', encoding='utf-8-sig') as arquivo:

            # Armazenando os dados dos usuários na lista 'DADOS'
            for linha in arquivo:
                informacao = linha.strip().split(",")

            # Verifica se a linha tem exatamente 3 campos
                if len(informacao) == 3:  
                    DADOS.append(informacao)

    # Tratando exceções caso o arquivo não exista ou esteja vazio
    except FileNotFoundError:
        print(f"\n🛑 Arquivo de Dados não Encontrado.")
        return
    
    except Exception as e:
        print(f"\n❗ Ocorreu um erro ao acessar o arquivo: {e}")
        return

    # Variável para notificar a tentativa de login de um usuário não cadastrado no sistema
    encontrado = False

    for informacoes in DADOS:
        
        # Verificando o nome do perfil cadastrado (normalizando para evitar erros)
        if informacoes[0].strip().lower() == nome_usuario.strip().lower():
            encontrado = True

            # Verificando se a senha informada é a mesma que a senha cadastrada
            if informacoes[1].strip() != senha_informada.strip():
                print(f"\n❌ Usuário e/ou senha inválidos!")
                return

            # Se a senha estiver correta
            print(f"\n✅ Login Bem - Sucedido!")

            # Verificando se o usuário é administrador
            if len(informacoes) > 2 and informacoes[2].strip().lower() == 'administrador':
                # Abre o menu do administrador
                menu_administrador()

            # Se for um usuário casual
            else:
                # Abre o menu do usuário casual e passa o nome do usuário
                menu_casual(nome_usuario)
            return

    if not encontrado:
        print(f"\n🟨 Usuário não Cadastrado.")

    # Limpa a informação da lista 'DADOS' para o próximo input de informações
    DADOS.clear()


