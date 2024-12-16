"Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno." 
"A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11)." 
"Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal."

def media1():

    nota1 = float(input("Informe sua primeira nota:")) #Usuario irá informar um valor referente à nota1
    nota2 = float(input("Informe sua segunda nota:")) #Usuario irá informar um valor referente à nota2

    MEDIA = ((nota1 * 3.5) + (nota2 * 7.5)) / 11 #Formula para calcular media

    #Condicionais para verificação das notas informadas
    if nota1 > 10 or nota1 < 0:
        print("Insira um valor válido para a primeira nota!")

    elif nota2 > 10 or nota2 < 0:
        print("Insira um valor válido para a segunda nota!")

    else:
        print(f"MEDIA = {MEDIA:.5f}") #Mostra a MEDIA, caso as condições acima não se cumpram

if __name__ == "__media1__":
    media1()

def main():
    media1()
if __name__ == "__main__":
    main()

