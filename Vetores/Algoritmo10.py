"Considere	um	vetor	de	inteiros,	com	capacidade	de	10	valores.	Leia	do	usuá rio	um	valor	inicial	"
"de	 referência.	 Então,	 preencha	 o	 vetor	 de	 tal	 forma	 que	 o	 valor	 de	 referência	 deve	 ser"	
"armazenado no	centro	do	vetor,	entã o	o	valor	de	referência	será	incrementado em	1.	O	novo"	
"valor	de	referência	deve	ser	armazenado	nas	posiçõ es	anterior e	posterior ao	centro e	assim"	
"sucessivamente,	até	preencher	o	vetor	até	as	pontas"


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
