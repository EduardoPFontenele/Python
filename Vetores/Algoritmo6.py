"Escreva	um	algoritmo	que	utilize um	vetor	de	inteiros	com	capacidade	de	10	valores.Preencha"	
"o	vetor	com	valores	informados	pelo	usuário.	Então,	encontre	e	imprima	o	menor e	o	maior"
"valor	presente	no	vetor."

def maior_e_menor():

    VETOR = [] #Criando um vetor de n espaços

    #Laço para o usuario informar 10 numeros e guarda-los dentro do vetor
    for i in range(10):
        numeros = int(input(f"Digite um numero respectivo da posição [{i}]: "))
        VETOR.append(numeros)

    #Funções para buscarem o maior e o menor numero dentro do vetor
    maior = max(VETOR)
    menor = min(VETOR)

    print(f"Vetor: {VETOR}") #Mostra VETOR
    print(f"Maior numero: {maior}") #Mostra o maior elemento do vetor
    print(f"Menor numero: {menor}") #Mostra o menor elemento do vetor

if __name__ == "__maior_e_menor__":
    maior_e_menor()

def main():
    maior_e_menor()
if __name__ == "__main__":
    main()