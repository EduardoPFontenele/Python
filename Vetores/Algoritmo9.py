"Considere	um	vetor	de	inteiros,	com	capacidade	de	10	valores.	Leia	do	usuário	um	valor	inicial"	
"de	 referência.	 Então, preencha o	 vetor  de tal forma	 que  o	 valor	 de	 referência deve ser"	
"armazenado	das	pontas	do	vetor,	entã o	este valor	será	incrementado em	1.	O novo	valor deve"	
"ser armazenado	respectivamente	na	segunda	e penúltima posição e assim	sucessivamente."

def algoritmo9():

    #Criando três vetores de n espaços
    VETOR1 = []
    VETOR2 = []
    VETOR3 = []

    #Usuario informa um numero e o mesmo é guardado dentro de VETOR1
    referencia = int(input("Informe o numero referente à posição [0]: "))
    VETOR1.append(referencia)

    #Laço para preencher VETOR1, incrementando +1 dado o numero informado
    for i in range(1,5):
        VETOR1.append(VETOR1[i - 1] + 1)
    
    #Laço para inverter as posições de VETOR1 e guardar dentro de VETOR2
    for j in range(len(VETOR1) - 1, -1, -1):
        VETOR2.append(VETOR1[j])

    #VETOR3 armazenará os elementos de VETOR1 e VETOR2
    VETOR3 = VETOR1 + VETOR2

    print(VETOR3) #Mostra VETOR3
        
if __name__ == "__algoritmo9__":
    algoritmo9()

def main():
    algoritmo9()
if __name__ == "__main__":
    main()