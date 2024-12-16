"Escreva um algoritmo que utilize dois vetores de inteiros com capacidade de 5. O usuário deverá"
"informar os valores que serão armazenados no primeiro vetor. Então o sistema deve preencher o"
"segundo vetor com os valores do primeiro, mas em ordem contrária."

def ordem_contraria():

    #Criando dois vetores de tamanho n
    VETOR1 = []
    VETOR2 = []

    #Laço para o usuario informar 5 numeros e guarda-los dentro de VETOR1
    for i in range(5):
        numeros = int(input(f"Digite um numero respectivo da posição [{i}]: "))
        VETOR1.append(numeros)

    #Laço para posicionar os numeros armazenddos no VETOR1 em ordem contrária dentro do VETOR2
    for j in range(len(VETOR1) - 1, -1, -1):
        VETOR2.append(VETOR1[j])

    print(f"Vetor original: {VETOR1}") #Mostra VETOR1
    print(f"Vetor contrário: {VETOR2}") #Mostra VETOR2

if __name__ == "__ordem_contraria__":
    ordem_contraria()

def main():
    ordem_contraria()
if __name__ == "__main__":
    main()
        