def exibir_ranking():

    try:
        # Abrindo o arquivo no modo escrita e tratando possíveis conflitos de caracteres especiais com encoding='latin-1'
        with open('dados.txt', 'r', encoding='latin-1') as arquivo: 
            conteudo = arquivo.read().strip()
            
            # Verificando se o arquivo 'dados' não está vazio
            if not conteudo:
                print("\n❗ O arquivo 'dados.txt' está vazio!")
                return

            ranking = []

            # Armazenando os dados do arquivo na lista de forma padronizada
            for linha in conteudo.splitlines():
                dados = linha.strip().split(',')

                if len(dados) == 3:
                    nome, senha, pontos = dados

                    if pontos.isdigit():
                        # Iterando o terceiro elemento de dados 'pontos' como inteiro
                        ranking.append([nome, int(pontos)])

        # Ordenando o ranking manualmente (em ordem decrescente)
        for linha in range(len(ranking)):
            for coluna in range(linha + 1, len(ranking)):
                if ranking[linha][1] < ranking[coluna][1]:
                    ranking[linha], ranking[coluna] = ranking[coluna], ranking[linha]

        # Exibindo o ranking 
        print("\n🏆 Ranking de Pontuação:")
        
        if ranking:
            for posicao, item in enumerate(ranking, start=1):
                nome, pontos = item
                print(f"{posicao}. {nome} - ⭐{pontos} pontos")

        # Verificando se pessoas cadastradas no ranking
        else:
            print("Nenhum dado disponível no ranking.")

    # Tratando exceções caso o arquivo não exista / houve erro ao tentar acessá-lo
    except FileNotFoundError:
        print("\n❗Arquivo 'dados.txt' não existe. Verifique se ele existe.")
    except Exception as e:
        print(f"\n❗ Ocorreu um erro ao exibir o ranking: {e}")
