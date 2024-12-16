"Escreva um algoritmo que, utilizando um vetor de inteiros, com capacidade de 5 valores, conte e"
"armazene os valores de 5 até 1."

def contador():

    VETOR = [] #Criando um vetor de n espaços

    for i in range (5,0,-1): #Para numeros num alcance de 5 à 1, ao passo de -1
        VETOR.append(i) #Guardar numeros dentro do vetor

    print(VETOR) #Mostra vetor

if __name__ == "__contador__":
    contador()

def main():
    contador()
if __name__ == "__main__":
    main()