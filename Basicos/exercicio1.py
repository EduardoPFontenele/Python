"Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B "
"atribuindo o seu resultado na variável X. Imprima X conforme exemplo apresentado abaixo." 
"Não apresente mensagem alguma além daquilo que está sendo especificado e não esqueça de imprimir" 
"o fim de linha após o resultado, caso contrário, você receberá Presentation Error"

def somar():

    A = int(input("Digite um numero inteiro:")) #Usuario irá informar um valor referente à A
    B = int(input("Digite outro numero inteiro:")) #Usuario irá informar um valor referente à B

    X = A + B #A variável X irá receber o resultado da soma de A e B

    print(f"X = {X}") #Mostra X

if __name__ == "__somar__":
    somar()

def main():

    somar()
    
if __name__ == "__main__":
    main()