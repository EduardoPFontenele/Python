def criar_lista(lista,len):

    for i in range(len):
        numero = int(input(f"Digite o {i+1}º numero: "))
        lista.append(numero)

    print(f"\nLISTA = {lista}")

def definir_conjunto(lista):

    conjunto = set(lista)
    print(f"CONJUNTO = {conjunto}")


def main():

    LISTA = []
    tamanho = int(input(f"Informe quantos elementos deseja inserir na lista: "))

    if tamanho < 0:
        print(f"\nTamanho de lista invalido!")
    
    else:
        criar_lista(LISTA,tamanho)
        definir_conjunto(LISTA)

if __name__ == "__main__":
    main()

