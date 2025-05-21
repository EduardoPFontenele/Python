def verificar_arquivo(nome_arquivo):

    try:
        with open(nome_arquivo,'r') as arquivo:
            conteudo = arquivo.read()

    except FileNotFoundError:
        print(f"-" * 30)
        print(f"ERRO: Arquivo Não Encontrado!")
    
    else:
        print(f"CONTEUDO = {conteudo}")
    
    finally:
        print(f"Encerrando Leitura de Arquivo!")
        print(f"-" * 30)
    
def main():

    verificar_arquivo('Inexistente.txt')

if __name__ == "__main__":
    main()