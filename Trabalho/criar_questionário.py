def cadastrar_pergunta(nome_arquivo, enunciado, resposta, lista_alternativas, dificuldade):

    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
        # Escreve o nível no próprio enunciado
        arquivo.write(f"({dificuldade}) {enunciado}\n")

        for alt in lista_alternativas:
            arquivo.write(f"{alt}\n")

        arquivo.write(f"Resposta: {resposta}\n")