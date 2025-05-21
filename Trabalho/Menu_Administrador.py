from criar_questionário import cadastrar_pergunta
from ranking import exibir_ranking

def menu_administrador():

    ALTERNATIVAS = []
    DIFICULDADES = ['fácil','média','difícil']
    OPCOES = ['a','b','c','d']

    # Menu Iterativo para o Administrador
    while True:
        print(f"""
╔════════════════════════════════════╗
║      👑 MENU DO ADMINISTRADOR      ║
╠════════════════════════════════════╣
║  1. ✍️  Cadastrar Pergunta          ║
║  2. 📊 Ver Ranking                 ║
║  0. 🚪 Sair                        ║
╚════════════════════════════════════╝
""")
        try:
            # Coletando informações do usuário
            opcao = int(input(f"➡️  Escolha a opção que deseja realizar: "))

            if opcao == 1:
                print(f"""
    ╔════════════════════════════════════════════════╗
    ║           ❔ CADASTRO DE PERGUNTAS             ║  
    ╠════════════════════════════════════════════════╣""")
                
                enunciado = input(f"💭 Enunciado: ").strip()

                #Verificando se o imput de 'enunciado' é vazio
                if not enunciado:
                    print("\n❗ O enunciado não pode estar vazio!")
                    continue

                for i in range(4):
                    alternativa = input(f"Opção {i+1}: ").strip()

                    #Verificando se o imput de 'alternativa' é vazio
                    if not alternativa:
                        print("\n❗ As alternativas não podem estar vazias!")
                        break
                    
                    ALTERNATIVAS.append(alternativa)

                # Usuário irá definir a dificuldade do enunciado
                dificuldade = input(f"🤔 Dificuldade (Fácil / Média / Difícil / Misto): ")

                #Verificando se a dificuldade digitada pelo usuário é a mesma definida no sistema
                if dificuldade.lower() not in DIFICULDADES:
                    print(f"\n❗ Defina uma Dificuldade Válida!")

                else:

                    # Usuário irá definir a resposta do enunciado
                    resposta = input(f"\n🔍 Letra da Opção Correta (a/b/c/d): ")

                    #Verificando se a resposta do enunciando é válida (a,b,c,d)
                    if resposta.lower() not in OPCOES:
                        print(f"\n❗Opção de Resposta Inválida.")
                    
                    else:

                        if dificuldade.lower() == 'fácil':
                            cadastrar_pergunta('perguntas_nivel_facil.txt',
                                            enunciado, resposta.lower(), ALTERNATIVAS, 'fácil')
                            cadastrar_pergunta('perguntas_mistas.txt',
                                            enunciado, resposta.lower(), ALTERNATIVAS, 'fácil')
                        elif dificuldade.lower() == 'média':
                            cadastrar_pergunta('perguntas_nivel_medio.txt',
                                            enunciado, resposta.lower(), ALTERNATIVAS, 'média')
                            cadastrar_pergunta('perguntas_mistas.txt',
                                            enunciado, resposta.lower(), ALTERNATIVAS, 'média')
                        elif dificuldade.lower() == 'difícil':
                            cadastrar_pergunta('perguntas_nivel_dificil.txt',
                                            enunciado, resposta.lower(), ALTERNATIVAS, 'difícil')
                            cadastrar_pergunta('perguntas_mistas.txt',
                                            enunciado, resposta.lower(), ALTERNATIVAS, 'difícil')
                        # ...
                        ALTERNATIVAS.clear()

            #Irá exibir o ranking do usuário com mais acertos
            elif opcao == 2:
                exibir_ranking()

            #Fechará o menu do administrador e retornará para o Menu Principal
            elif opcao == 0:
                print(f"\n🏃 Retornando ao Menu Principal . . .")
                break
            
            #Verificando se a opção digitada é a mesma definida no sistema (1,2,0)
            else:
                print(f"\n🛑 Opção Inválida. Tente Novamente")

        #Tratamento de erro caso o valor digitado na variável 'opção' não seja um inteiro
        except ValueError:
            print(f"\n❗Valor Inválido. Digite a opção novamente.")

