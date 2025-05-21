def tabuada():

    numero = int(input("Informe um numero para realizar a tabuada:")) #Pede ao usuario um numero para mostrar a tabuada
    soma_sucessiva = 0 #inicializando soma_sucessiva com 0

    for i in range(1,11):  #Para i num alcance de 1 a 10
        
        soma_sucessiva += numero #soma_sucessiva recebe numero "i" vezes
        print(f"{numero} x {i} = {soma_sucessiva}") #Mostra tabuada

if __name__ == "__tabuada__":
    tabuada()

def main():
    tabuada()
if __name__ == "__main__":
    main()