"Escreva	um	algoritmo	que	utilize	um	vetor	de	inteiros	com	capacidade	de	10	valores.Leia do"	
"usuário apenas um	 valor e armazene na primeira posição do vetor. Em	seguida calcule e"
"preencha as	próximas posições	do	vetor de	tal	modo que	cada	posição	deve	receber	o	dobro	do"	
"valor	da	posição anterior."

def dobro3():

    #Criando um vetor de espaço n 
    VETOR = []

    #Usuario informar um numero, e o mesmo é armazenado na posição 0 do vetor
    numero = int(input(f"Digite um numero respectivo da posição [0]: "))
    VETOR.append(numero)
    
    #Laço para dobrar e precher os 9 espaços restantes do vetor
    for i in range(1,10):
        VETOR.append(VETOR[i - 1] * 2)
    
    print(f"{VETOR}") #Mostra VETOR

if __name__ == "__dobro3__":
    dobro3()

def main():
    dobro3()
if __name__ == "__main__":
    main()




