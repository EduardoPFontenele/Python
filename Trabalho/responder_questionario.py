def mostrar_enunciado(nome_arquivo, dificuldade, nome_usuario):
    try:
        with open(nome_arquivo, 'r', encoding='latin-1') as arquivo:
            linhas = [l.strip() for l in arquivo.read().splitlines() if l.strip()]
    except FileNotFoundError:
        print(f"\n❗Arquivo '{nome_arquivo}' não existe.")
        return 0, 0  # Retorna 0 acertos e 0 pontos em caso de erro

    if not linhas:
        print(f"\n❗ O arquivo '{nome_arquivo}' está vazio!")
        return 0, 0  # Retorna 0 acertos e 0 pontos se o arquivo estiver vazio

    # Agrupa de 6 em 6 (enunciado + 4 alternativas + resposta) sem list comprehension
    perguntas = []
    for i in range(0, len(linhas), 6):
        bloco = linhas[i:i+6]
        if len(bloco) == 6:  # Garante que o bloco tem exatamente 6 linhas
            perguntas.append(bloco)

    acertos = 0
    pontos = 0
    pts = {'fácil': 1, 'média': 2, 'difícil': 3}

    for bloco in perguntas:
        print(f"\n❓ {bloco[0]}")
        print(f"A) {bloco[1]}")
        print(f"B) {bloco[2]}")
        print(f"C) {bloco[3]}")
        print(f"D) {bloco[4]}")

        correta = bloco[5].replace("Resposta: ", "").strip().lower()
        resp = input("\n📝 Sua resposta: ").lower()

        if resp == correta:
            print("\n✅ Resposta Correta!")
            acertos += 1
            pontos += pts.get(dificuldade, 0)
        else:
            print("\n❌ Resposta Incorreta.")
            print(f"✔️ A resposta correta era: {correta.upper()}")  # Exibe a resposta correta

    # Atualiza só se ganhou algo
    if pontos > 0:
        atualizar_pontuacao(nome_usuario, pontos)

    print(f"\n🎉 Você acertou {acertos} pergunta(s) e fez {pontos} ponto(s)!")
    return acertos, pontos  # Retorna os resultados


def atualizar_pontuacao(nome_usuario, pontos_a_incrementar):
    linhas = []
    usuario_encontrado = False
    
    # Abrindo o arquivo no modo leitura e tratando possíveis conflitos de caracteres especiais com encoding='latin-1'
    with open('dados.txt', 'r', encoding='latin-1') as arquivo:  
        # Lendo as informações do arquivo 'dados'
        for linha in arquivo:
            dados = linha.strip().split(',')

            # Verificando o nome do usuário e sua respectiva pontuação
            if dados[0].strip().lower() == nome_usuario.strip().lower():
                usuario_encontrado = True
                # Verifica se o terceiro campo é um número antes de atualizar a pontuação
                if dados[2].isdigit():
                    dados[2] = str(int(dados[2]) + pontos_a_incrementar)
                else:
                    print(f"\n❗ Usuário '{nome_usuario}' não pode ter a pontuação atualizada (não é um usuário casual).")
                    return

            linhas.append(dados)

    # Se o usuário não foi encontrado, exibe uma mensagem de erro
    if not usuario_encontrado:
        print(f"\n❗ Usuário '{nome_usuario}' não encontrado no arquivo 'dados.txt'.")
        return

    # Abrindo o arquivo no modo escrita e tratando possíveis conflitos de caracteres especiais com encoding='latin-1'
    with open('dados.txt', 'w', encoding='latin-1') as arquivo:  
        for dados in linhas:
            # Atualiza a pontuação do usuário no arquivo
            linha_atualizada = f"{dados[0]},{dados[1]},{dados[2]}\n"
            arquivo.write(linha_atualizada)