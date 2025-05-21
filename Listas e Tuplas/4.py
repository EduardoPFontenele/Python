def gerar_lista_inteiros(lista):

    #Coleta de dados do usuario
    numero = int(input(f"Informe o tamanho da lista de numeros inteiros que deseja gerar: "))

    #Gerar uma lista de numeros inteiros até n (informado pelo usuario)
    if numero > 0: 
        for i in range(1,numero + 1):
            lista.append(i)

        print(f"-" * 30)
        print(f"Lista gerada com sucesso!")
        print(f"-" * 30)
    
    #Gerar uma lista de numeros inteiros negativos até n (informado pelo usuario)
    elif numero < 0:
        numero = numero * (-1)
        for i in range (1,numero + 1):

            lista.append(i * (-1))
    
        print(f"-" * 30)
        print(f"Lista gerada com sucesso!")
        print(f"-" * 30)
    
    #Caso o tamanho da lista seja igual a 0
    else:
        print(f"\nTamanho de lista invalido!")

def impares(lista):

    #Verificando se a lista existe
    if len(lista) <= 0:
        print(f"Lista Inexistente e/ou de Tamanho invalido!")
    
    else: 
        
        #Mostrando a lista com todos os inteiros
        print(f"LISTA =  {lista}")
        fatiar_impares = lista[0:len(lista):2]

        #Mostrando todos os elementos impares da lista utilizando slicing
        print(f"IMPARES = {fatiar_impares}")

def main():

    NUMEROS = []

    #Menu com varias opções para o usuario selecionar a operação que deseja realizar
    while True:
        print(f"\n<< FILTRANDO NUMEROS IMPARES >>\n")
        print(f"1. Gerar uma lista de numeros inteiros.")
        print(f"2. Mostrar Impares.")
        print(f"3. Finalizar programa.")

        opcao = int(input(f"\nInforme a operação que deseja realizar: "))

        if opcao == 1:
            print(f"\n<< GERAR LISTA >>\n")
            gerar_lista_inteiros(NUMEROS)
        
        elif opcao == 2:
            print(f"\n<< LISTA DOS NUMEROS IMPARES >>\n")
            impares(NUMEROS)
        
        elif opcao == 3:
            print(f"\nFinalizando . . .")
            break

        else:
            print(f"\nOpção Inválida!")
    
if __name__ == "__main__":
    main()