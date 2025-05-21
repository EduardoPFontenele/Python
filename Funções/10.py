"""
Defina uma funcao chamada celsius para kelvin que recebe uma temperatura em graus
Celsius e a converte para Kelvin. A formula de conversao eh: K = C + 273.15.
"""

def print_formatado(texto):

    #Deixando print destacado
    
    print(f"-" * 30)
    print(f"{texto}")
    print(f"-" * 30)

def celsius_para_kelvin(Celsius):

    #Logica para a resolucao do exercicio
    conversao = Celsius + 273.15 
    print_formatado(f"{Celsius} Celsius = {conversao} Kelvin")

def main():
    
    #Coletando informacoes do usuario
    Celsius = float(input(f"-> Informe a temperatura (Celsius): "))
    celsius_para_kelvin(Celsius)

if __name__ == "__main__":
    main()