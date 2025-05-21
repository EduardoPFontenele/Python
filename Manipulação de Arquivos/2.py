def adicionar_texto(dicionario_texto):
    
    #Criando um dicionario vazio
    dicionario_texto = {}

    #Abrindo o arquito 'relatorio.txt'
    with open('relatorio.txt','r') as arquivo:

        #Percorrendo a linha do arquivo
        texto = arquivo.readline()

        #Transformar a linha em uma lista separada por virgulas
        texto_separado = texto.split()

        #Pecorrendo a lista 'texto_separado'
        for palavras in texto_separado:
            #Contando as ocorrencias de palavras
            if palavras in dicionario_texto:
                dicionario_texto[palavras] += 1

            else:
                dicionario_texto[palavras] = 1
    
    #Mostrar o total de palavras da frase
    total_palavras = len(texto_separado)

    #Adquirir a palavra com o maior numeros de ocorrencias
    palavra_frequente = max(dicionario_texto, key=dicionario_texto.get)

    print(f"Total de Palavras: {total_palavras}")
    print(f"Palavra mais Frequente: {palavra_frequente}")

def main():
    PALAVRAS = {}
    adicionar_texto(PALAVRAS)

if __name__ == "__main__":
    main()