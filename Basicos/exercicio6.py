"Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença"
"do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D)."

def diferenca_produtos():

    valor1 = int(input("Insira o valor de A:")) #Usuario irá informar um valor referente à valor1
    valor2 = int(input("Insira o valor de B:")) #Usuario irá informar um valor referente à valor2
    valor3 = int(input("Insira o valor de C:")) #Usuario irá informar um valor referente à valor3
    valor4 = int(input("Insira o valor de D:")) #Usuario irá informar um valor referente à valor4

    DIFERENCA = (valor1 * valor2) - (valor3 * valor4) # Formula para calcular a diferença entre os produtos


    print(f"DIFERENÇA = {DIFERENCA}") #Mostra DIFERENÇA

if __name__ == "__diferenca_produtos__":
    diferenca_produtos()

def main():
    diferenca_produtos()
if __name__ == "__main__":
    main()