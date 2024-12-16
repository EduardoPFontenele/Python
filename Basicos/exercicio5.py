def media2():
    nota1 = float(input("Informe a sua primeira nota:")) #Usuario irá informar um valor referente à nota1
    nota2 = float(input("Informe a sua segunda nota:")) #Usuario irá informar um valor referente à nota2
    nota3 = float(input("Informe a sua terceira nota:")) #Usuario irá informar um valor referente à nota3

    MEDIA = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10 #Formula para calcular a media das três notas

    #Condicionais para verificação das notas informadas
    if nota1 > 10 or nota1 < 0:
        print("Insira um valor válido para a primeira nota!")

    elif nota2 > 10 or nota2 < 0:
        print("Insira um valor válido para a segunda nota!")

    elif nota3 > 10 or nota3 < 0:
        print("Insira um valor válido para a terceira nota!")

    else:
        print(f"MEDIA = {MEDIA:.1f}") #Mostra a MEDIA, caso as condições acima não se cumpram

if __name__ == "__media2__":
    media2()

def main():
    media2()
if __name__ == "__main__":
    main()
    