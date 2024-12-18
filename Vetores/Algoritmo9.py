"Considere	um	vetor	de	inteiros,	com	capacidade	de	10	valores.	Leia	do	usuário	um	valor	inicial"	
"de	 referência.	 Então, preencha o	 vetor  de tal forma	 que  o	 valor	 de	 referência deve ser"	
"armazenado	das	pontas	do	vetor,	entã o	este valor	será	incrementado em	1.	O novo	valor deve"	
"ser armazenado	respectivamente	na	segunda	e penúltima posição e assim	sucessivamente."

def algoritmo9():

    VETOR = [] #Criando um vetor de n espaços
    referencia = int(input("Informe um numero referencia: ")) #Usuario irá informar um valor referência

    for i in range(0,5):

        incremento = referencia + i #variável para incrementar à referencia
        VETOR.append(incremento)
    
    for j in range(0,5):
        decremento = referencia + 4 - j # Variável para decrementar a partir do último valor crescente
        VETOR.append(decremento)


    print(VETOR) #Mostra vetor

def main():
    algoritmo9()
if __name__ == "__main__":
    main()
