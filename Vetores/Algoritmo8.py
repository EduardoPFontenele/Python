"Escreva	um	algoritmo	que	utilize	um	vetor	de	inteiros	com	capacidade	de	10	valores.	Leia	do"	
"usuário	dois	valores	e armazene	nas	duas	primeiras	posiçõ es	do	vetor.	As	posiçõ es	seguintes"	
"deverão	ser	calculadas	de	tal	forma	que	cada	posiçã o calculada deve	recebera	soma	das	duas"	
"posições anteriores."

def soma_sucessiva():

    VETOR = [] #Criando um vetor de n espaços

    #Laço para o usuario informar 2 numeros e guarda-los dentro do vetor
    for i in range(2):
        numeros = int(input(f"Digite um numero respectivo da posição [{i}]: "))
        VETOR.append(numeros)

    #Laço para preencher o vetor pela soma das posições anteriores
    for j in range(2,10):
        VETOR.append(VETOR[j - 2] + VETOR[j - 1])

    print(f"{VETOR}") #Mostra VETOR

if __name__ == "__soma_sucessiva__":
    soma_sucessiva()

def main():
    soma_sucessiva()
if __name__ == "__main__":
    main()