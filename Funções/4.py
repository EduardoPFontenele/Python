"""
Defina uma funcao chamada calculo imc que recebe a altura e o peso de uma pessoa e calcula
seu Indice de Massa Corporal (IMC). A funcao deve retornar a categoria do IMC de acordo
com a tabela:
Abaixo do peso: IMC < 18.5
Peso normal: 18.5 <= IMC < 24.9
Sobrepeso: 25 <= IMC < 29.9
Obesidade: IMC >= 30
"""
def Calculo_IMC(peso,altura):
    
    #Verificacao das entradas do usuario
    if peso <= 0 or altura <= 0:
        return "Insira valores válidos!"
    
    else:
    
    #Logica para a resolucao do exercicio
        IMC = peso / (altura ** 2)
        
        print(f"IMC = {IMC:.2f}")

        if IMC < 18.5:
            return "Abaixo do peso."
        
        elif IMC <= 24.9:
            return "Peso normal."
        
        elif IMC <= 29.9:
            return "Sobrepeso."
        
        else:
            return "Obesidade."


def main():

    #Colentado dados do usuario
    peso = float(input(f"-> Informe seu peso (kg): "))
    altura = float(input(f"-> Informe sua altura (m): "))

    print(f"{Calculo_IMC(peso,altura)}")

if __name__ == "__main__":
    main()