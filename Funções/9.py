"""
Defina uma funcao chamada serie potencias que recebe um numero inteiro n e calcula a
soma da serie: 1^2 + 2^2 + 3^2 + . . . + n^2
"""

def print_formatado(texto):

    #Deixando print destacado
    print(f"-" * 30)
    print(f"{texto}")
    print(f"-" * 30)

def serie_potencias(numero):

    #Logica para a resolucao do problema
    soma = 0

    for i in range(1, numero + 1):
        soma += i ** 2
    
    print_formatado(f"SOMATORIO DA SERIE = {soma}")

def main():
    
    #Colentando informações do usuario
    numero = int(input(f"-> Informe o tamanho da serie: "))
    serie_potencias(numero)

if __name__ == "__main__":
    main()