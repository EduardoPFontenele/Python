def notas():

    #Laço para usuario informar 10 notas
    for i in range(10):
        nota = float(input("Informe sua nota:"))

    #Condicionais para a verificacao da nota
        if nota < 0 or nota > 10:
            print(f"Nota inválida!")
        
        elif nota >= 7:
            print(f"Aprovado!")
        
        else:
            print(f"Reprovado")

if __name__ == "__notas__":
    notas()

def main():
    notas()
if __name__ == "__main__":
    main()