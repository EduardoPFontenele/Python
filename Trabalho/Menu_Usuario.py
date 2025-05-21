from responder_questionario import mostrar_enunciado
from ranking import exibir_ranking

def menu_casual(nome_usuario): 

    ENUNCIADO = []  # Lista para armazenar o enunciado das perguntas
    DIFICULDADES = ['facil', 'media', 'dificil', 'misto']  # Níveis disponíveis
    
    while True:
        print(f"""
╔════════════════════════════════╗
║      👤 MENU DO USUARIO        ║
╠════════════════════════════════╣
║  1. 🧠 Fazer Quiz              ║
║  2. 📊 Ver Ranking             ║  
║  0. 🚪 Sair                    ║
╚════════════════════════════════╝""")
        try:
            
            opcao = int(input(f"➡️  Escolha a opção que deseja realizar: "))

            if opcao == 1:
                dificuldade = input(f"📊Escolha o Nível de Dificuldade (facil / media / dificil / misto): ").strip().lower()
                
                if dificuldade not in DIFICULDADES:
                    print("\n❗ Nível de dificuldade inválido! Tente novamente.")
                    continue
                
                total_acertos = 0
                total_pontos = 0

                if dificuldade == 'media':
                    acertos, pontos = mostrar_enunciado('perguntas_nivel_medio.txt', 'média', nome_usuario)
                    total_acertos += acertos
                    total_pontos += pontos
                    
                elif dificuldade == 'dificil':
                    acertos, pontos = mostrar_enunciado('perguntas_nivel_dificil.txt', 'difícil', nome_usuario)
                    total_acertos += acertos
                    total_pontos += pontos
                    
                elif dificuldade == "facil":
                    acertos, pontos = mostrar_enunciado('perguntas_nivel_facil.txt', 'fácil', nome_usuario)
                    total_acertos += acertos
                    total_pontos += pontos
                    
                elif dificuldade == "misto":
                    # Processa perguntas de todas as categorias e acumula os resultados
                    for arquivo, nivel in [
                        ('perguntas_nivel_facil.txt', 'fácil'),
                        ('perguntas_nivel_medio.txt', 'média'),
                        ('perguntas_nivel_dificil.txt', 'difícil')
                    ]:
                        acertos, pontos = mostrar_enunciado(arquivo, nivel, nome_usuario)
                        total_acertos += acertos
                        total_pontos += pontos

                    print(f"\n🎉 Total de acertos: {total_acertos} pergunta(s).")
                    print(f"⭐ Total de pontos: {total_pontos} ponto(s).")

            elif opcao == 2:
                exibir_ranking()
            
            elif opcao == 0:
                print(f"\n🏃 Retornando ao Menu Principal . . .")
                break
            
            else:
                print(f"\n🛑 Opção Inválida. Tente Novamente")

        except ValueError:
            print(f"\n❗Valor Inválido. Digite a opção novamente.")