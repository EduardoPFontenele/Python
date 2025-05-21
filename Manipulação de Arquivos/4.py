def filtragem_logs(nome_arquivo,lista):

    #Abrindo o arquivo 'log,txt' 
    with open(nome_arquivo,'r') as arquivo:
        #Lendo as informações do arquivo
        informacoes = arquivo.readlines()
    
    #Percorrendo as informações dos logs
    for logs in informacoes:
        if 'Erro' in logs:
            with open('erros.txt','a') as arquivo_erros:
                arquivo_erros.write(logs)        

    with open('erros.txt','r') as arquivo2:
        dados = arquivo2.readlines()
    
    ocorrencia_erros = len(dados)
    print(f"{ocorrencia_erros} eventos de erro encontrados em 'erros.txt'")

def main():

    INFORMACOES = []
    filtragem_logs('log.txt',INFORMACOES )

if __name__ == "__main__":
    main()