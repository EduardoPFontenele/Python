"Escreva um algoritmo que utilize dois vetores de inteiros com capacidade de 5. O usuário deverá"
"informar os valores que serão armazenados no primeiro vetor. Então o sistema deve calcular o"
"dobro de cada valor e armazenar o resultado do cálculo no segundo vetor. Ao final, imprima o vetor"
"original (com os valores informados pelo usuário) e o vetor com o resultado do cálculo."

def dobrar2():

    #Criando dois vetores de n espaços 
    VETOR1 = [] 
    VETOR2 = []

    for i in range(5): #Laço para usuario informar 5 numeros
        numeros = int(input(f"Digite um numero respectivo da posição [{i}]: "))

        VETOR1.append(numeros) #Numeros informados são guardados dentro de VETOR1
        VETOR2.append(VETOR1[i] * 2) #Elementos do VETOR1 são guardados no VETOR2,multiplicando os elementos por 2 (dobro)

    print(f"Vetor original: {VETOR1}") #Mostra o VETOR1
    print(f"Vetor dobrado: {VETOR2}")  #Mostra o VETOR1    

if __name__ == "__dobrar2__":
    dobrar2()

def main():
    dobrar2()
if __name__ == "__main__":
    main()