"""
Defina uma funcao chamada conta consoantes que recebe uma string e conta o numero de
consoantes na string.
"""

def print_formatado(texto):

    #Deixando o print destacado
    print(f"-" * 30)
    print(f"{texto}")
    print(f"-" * 30)

def conta_consoantes(palavra):

    #Criando 2 vetores para armazenar vogais e consoantes
    VOGAIS = []
    CONSOANTES = []

    #Transformando a palavra informada em uma lista com os caracteres separados por virgulas
    lista_palavra = list(palavra)

    for i in range(len(lista_palavra)):
         #Verificando se há vogais na lista
        if lista_palavra[i] == "a" or lista_palavra[i] == "e" or lista_palavra[i] == "i" or lista_palavra[i] == "u"  or lista_palavra[i] == "o":

            #Armazenando vogais na lista VOGAIS
            VOGAIS.append(lista_palavra[i])

    #Verificando a existência de consoantes
    for letras in lista_palavra:
        if letras not in VOGAIS:
            
            #Armazenando as consoantes na lista CONSOANTES
            CONSOANTES.append(letras)

    #Função para verificar o tamanho da lista CONSOANTES
    quantidade_consoantes = len(CONSOANTES)

    print_formatado(f"{palavra}\nHá {quantidade_consoantes} consoantes!")

def main():

    #Coletando informacoes do usuario
    palavra = input(f"-> Digite uma palavra: ").lower() #Faz com que os caracteres sempre sejam minusculos

    conta_consoantes(palavra)

if __name__ == "__main__":
    main()