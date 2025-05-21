from datetime import datetime

def backup(nome_arquivo):

    #Abrindo o arquivo 'config.txt'
    with open(nome_arquivo, 'r') as arquivo:
        
        #Lendo as informações do arquivo
        texto = arquivo.read()

    #Definindo a data atual
    data_atual = datetime.now().strftime("%d/%m/%Y")

    #Abrindo o arquivo 'config backup.txt' 
    with open('config backup.txt', 'a') as arquivo_backup:

        #Escrevendo a data de hoje
        arquivo_backup.write(f"Backup criado em: {data_atual}\n\n")

        #transcrevendo os dados do arquivo 'config.txt'
        arquivo_backup.write(texto)

    print("Backup concluído com sucesso!")

def main():

    backup('config.txt')

if __name__ == "__main__":
    main()
