"Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e"
"atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem" 
"correspondente."   

def multiplicacao():

    numero1 = int(input("Digite um numero:")) #Usuario irá informar o valor referente ao numero1
    numero2 = int(input("Digite outro numero:")) #Usuario irá informar o valor referente ao numero2

    PROD = numero1 * numero2 #PROD recebe a multiplicao de numero1 e numero2

    print(f"PRODUTO = {PROD}") #mostra PROD

if __name__ == "__multiplicacao__":
    multiplicacao()

def main():
    multiplicacao()
if __name__ == "__main__":
    main()
