"Escreva um algoritmo que utilize um vetor de inteiros com capacidade de 10. O sistema deve ler do"
"usuário os 10 valores, armazenar no vetor e então calcular o dobro de cada valor e atualizar"
"respectivamente os valores no vetor. Ao final, imprima o vetor."

def dobrar():

    VETOR = [] #Criando um vetor de n espaços

    #Laço para o usuario informar 10 valores à serem armazenados dentro do vetor
    for i in range(10):

        numeros = int(input(f"Digite um numero respectivo da posição [{i}]: "))
        VETOR.append(numeros * 2) #Vetor guarda os numeros multiplicados por 2 (dobro)

    print(VETOR) # Mostra o vetor

if __name__ == "__dobrar__":
    dobrar()

def main():
    dobrar()
if __name__ == "__main__":
    main()