"""
Defina uma funcao chamada soma digitos que recebe um numero inteiro e retorna a soma de
seus digitos. Por exemplo, se a entrada for 123, a saida deve ser 6 (1 + 2 + 3).
"""

def print_formatado(texto):

    #Deixando o print destacado
    print(f"-" * 30)
    print(f"{texto}")
    print(f"-" * 30)

def soma_digitos(numero):

    #Crindo uma Lista para armazenar numeros inteiros
    LISTA_INTEIROS = []

    #Transformando o numero informado em uma string
    stringar_numero = str(numero)

    #Transformando a string em uma lista cujo os caracteres sao separados por virgulas
    lista_numero = list(stringar_numero)

    #Convertendo as strings em inteiros e armazendo na lista LISTA_INTEIROS
    for itens in lista_numero:
        LISTA_INTEIROS.append(int(itens))
    
    #Função para somar todos os elementos da lista
    soma_elementos = sum(LISTA_INTEIROS)

    print_formatado(f"{numero}\nSOMA DOS ELEMENTOS = {soma_elementos}")

def main():

    #Coletando informacoes do usuario
    numero = int(input(f"Informe um numero: "))
    soma_digitos(numero)

if __name__ == "__main__":
    main()