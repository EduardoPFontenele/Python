"""
Defina uma funcao chamada media tres numeros que recebe tres numeros e retorna a media
aritmetica deles.
"""

def media_três_numeros(A,B,C):

    #Logica para resolução do problmea
    media = (A + B + C) / 3
    return media

def main():

    #Coleta de Informações do Usuario
    A = int(input(f"-> Informe o 1o numero: "))
    B = int(input(f"-> Informe o 2o numero: "))
    C = int(input(f"-> Informe o 3o numero: "))

    print(f"({A} + {B} + {C}) / 3")
    print(f"{A + B + C} / 3")
    print(f"{media_três_numeros(A,B,C)}")

if __name__ == "__main__":
    main()