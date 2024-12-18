def algoritmo10():

    VETOR = [] #Criando um vetor de n espaços
    referencia = int(input("Informe o valor referencia: ")) #Usuario irá informar um numero "referencia"

    for i in range(0,5):

        incremento = referencia + i #Variavel para incrementar à referencia
        VETOR.insert(0,incremento) #Adicionando elementos no começo do vetor
        VETOR.append(incremento) #Adicionando elementos á frente do vetor

    print(VETOR) #Mostra VETOR


def main():
    algoritmo10()
if __name__ == "__main__":
    main()