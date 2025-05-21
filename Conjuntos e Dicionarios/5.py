def criar_listas(len,lista1,lista2):

    print(f"\n<===== LISTA 1 =====>\n")

    for i in range(len):
        elemento = input(f"Digite o {i+1}º elemento da lista: ")
        lista1.append(elemento)
    
    print(f"\nLISTA 1 = {lista1}")

    print(f"\n<===== LISTA 2 =====>\n")

    for j in range(len):
        elemento1 = input(f"Digite o {j+1}º elemento da lista: ")
        lista2.append(elemento1)
        
    print(f"\nLISTA 2 = {lista2}")    

def comparar_listas(lista1,lista2,len):

    IGUAIS = []

    for item in lista1:
        if item in lista2:
            IGUAIS.append(item)

    conjunto_iguais = set(IGUAIS)    
    print(f"\n<===== ELEMENTOS IGUAIS =====>\n")
    print(f"{conjunto_iguais}")

def main():

    LISTA1= []
    LISTA2= []

    tamanho = int(input(f"Informe o tamanho de ambas as listas: "))

    if tamanho < 0:
        print(f"Tamanho de lista inválido!")

    else:
        criar_listas(tamanho,LISTA1,LISTA2)
        comparar_listas(LISTA1,LISTA2,tamanho)

if __name__ == "__main__":
    main()
    