"""
Defina uma funcao chamada conta digitos que recebe um numero inteiro e retorna a quantidade de digitos presentes nesse numero
"""

def print_formatado(texto):

    #Deixando o print destacado
    print(f"-" * 30)
    print(f"{texto}")
    print(f"-" * 30)

def conta_digitos(numero):

    #Transformando o numero informado em uma string
    stringar_numero = str(numero)

    #Transformando a string em uma lista com os caracteres separados por virgulos
    lista_numero = list(stringar_numero)

    #Função para saber o tamanho da lista
    quantidade_digitos = len(lista_numero)

    print_formatado(f"{numero}\nQUANTIDADE DE DIGITOS = {quantidade_digitos}")

def main():

    #Coletando informações do usuario
    numero = int(input(f"-> Informe um numero inteiro: "))
    conta_digitos(numero)

if __name__ == "__main__":
    main()
    